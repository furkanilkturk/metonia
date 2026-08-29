from __future__ import annotations

import contextlib
import importlib.util
import io
import shutil
import tempfile
import unittest
from pathlib import Path


REPOSITORY = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("metonia_validate", REPOSITORY / "scripts" / "validate.py")
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)


class RemoteIdentityTests(unittest.TestCase):
    def test_remote_forms_normalise_to_one_identity(self) -> None:
        forms = (
            "https://github.com/Example-Company/Atlas-Notes.git",
            "https://github.com/Example-Company/Atlas-Notes.git/",
            "ssh://git@github.com/Example-Company/Atlas-Notes.git",
            "git@github.com:Example-Company/Atlas-Notes.git",
            "github.com/Example-Company/Atlas-Notes.git",
        )
        identities = {VALIDATOR.normalise_remote(remote) for remote in forms}
        self.assertEqual(identities, {"github.com/example-company/atlas-notes"})

    def test_duplicate_cross_form_remote_fails_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = Path(temporary) / "metonia"
            shutil.copytree(
                REPOSITORY,
                fixture,
                ignore=shutil.ignore_patterns(".git", "__pycache__"),
            )
            duplicate = fixture / "template" / "Work" / "Companies" / "Duplicate Company"
            (duplicate / "Projects" / "Duplicate Atlas").mkdir(parents=True)
            shutil.copyfile(
                fixture / "template" / "Work" / "Companies" / "_templates" / "Company.md",
                duplicate / "Company.md",
            )
            (duplicate / "AGENTS.md").write_text("# Duplicate Company\n", encoding="utf-8")
            (duplicate / "Projects" / "Duplicate Atlas" / "AGENTS.md").write_text(
                "# Duplicate Atlas\n", encoding="utf-8"
            )
            (duplicate / "Projects" / "Duplicate Atlas" / "Project.md").write_text(
                "---\n"
                "tags: [project, test]\n"
                "status: test\n"
                "company: Duplicate Company\n"
                "repository: git@github.com:example-company/atlas-notes.git\n"
                "repositories: []\n"
                "---\n\n"
                "# Duplicate Atlas\n",
                encoding="utf-8",
            )

            old_root, old_template = VALIDATOR.ROOT, VALIDATOR.TEMPLATE
            VALIDATOR.ROOT, VALIDATOR.TEMPLATE = fixture, fixture / "template"
            output = io.StringIO()
            try:
                with contextlib.redirect_stdout(output):
                    result = VALIDATOR.main()
            finally:
                VALIDATOR.ROOT, VALIDATOR.TEMPLATE = old_root, old_template

        self.assertEqual(result, 1)
        self.assertIn("duplicate repository identity", output.getvalue())

    def test_vendored_skill_hash_mismatch_fails_validation(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            fixture = Path(temporary) / "metonia"
            shutil.copytree(
                REPOSITORY,
                fixture,
                ignore=shutil.ignore_patterns(".git", "__pycache__"),
            )
            skill = (
                fixture
                / "template"
                / "Learning"
                / ".agents"
                / "skills"
                / "doc-learning"
                / "SKILL.md"
            )
            skill.write_text(skill.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8")

            old_root, old_template = VALIDATOR.ROOT, VALIDATOR.TEMPLATE
            VALIDATOR.ROOT, VALIDATOR.TEMPLATE = fixture, fixture / "template"
            output = io.StringIO()
            try:
                with contextlib.redirect_stdout(output):
                    result = VALIDATOR.main()
            finally:
                VALIDATOR.ROOT, VALIDATOR.TEMPLATE = old_root, old_template

        self.assertEqual(result, 1)
        self.assertIn("vendored skill hash mismatch", output.getvalue())


if __name__ == "__main__":
    unittest.main()
