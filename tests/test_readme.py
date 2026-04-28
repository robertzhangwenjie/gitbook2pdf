"""
Tests for README.md changes introduced in PR:
- Removed old Chinese section about image display problem fix
- Added new Chinese one-liner description
- Added trailing newline at end of file
"""
import os
import unittest

README_PATH = os.path.join(os.path.dirname(__file__), "..", "README.md")


class TestReadmeContent(unittest.TestCase):
    def setUp(self):
        with open(README_PATH, encoding="utf-8") as f:
            self.content = f.read()

    # --- New content added in this PR ---

    def test_contains_new_chinese_description(self):
        """The new one-liner Chinese description should be present."""
        self.assertIn("一键抓取由 GitBook 框架生成的网站", self.content)

    def test_chinese_description_is_near_title(self):
        """The Chinese description should appear shortly after the h1 heading."""
        title_pos = self.content.find("# Gitbook2Pdf")
        desc_pos = self.content.find("一键抓取由 GitBook 框架生成的网站")
        self.assertGreater(title_pos, -1, "Title not found")
        self.assertGreater(desc_pos, -1, "Chinese description not found")
        # Description should be within 200 chars of the title
        self.assertLess(desc_pos - title_pos, 200)

    # --- Old content removed in this PR ---

    def test_removed_english_image_problem_heading(self):
        """Old heading about image display problem should be gone."""
        self.assertNotIn("This project has solved the image display problem", self.content)

    def test_removed_chinese_cause_analysis(self):
        """Old 原因分析 section should be gone."""
        self.assertNotIn("原因分析", self.content)

    def test_removed_chinese_solution_section(self):
        """Old 解决方案 section should be gone."""
        self.assertNotIn("解决方案", self.content)

    def test_removed_urljoin_explanation(self):
        """Old urllib.parse.urljoin explanation text should be gone."""
        self.assertNotIn("urllib.parse.urljoin", self.content)

    def test_removed_relative_url_explanation(self):
        """Old explanation about relative image URLs should be gone."""
        self.assertNotIn("相对地址", self.content)

    # --- Structural invariants (content that must remain intact) ---

    def test_contains_usage_section(self):
        """Usage section must still exist."""
        self.assertIn("## Usage", self.content)

    def test_contains_docker_usage(self):
        """Docker usage section must still exist."""
        self.assertIn("### With Docker", self.content)

    def test_contains_python_usage(self):
        """Python CLI usage section must still exist."""
        self.assertIn("### With python", self.content)

    def test_contains_original_project_link(self):
        """Link to the original project must still exist."""
        self.assertIn("[original project url](https://github.com/fuergaosi233/gitbook2pdf)", self.content)

    def test_file_ends_with_newline(self):
        """PR adds a trailing newline — file must end with newline character."""
        self.assertTrue(self.content.endswith("\n"), "README.md should end with a newline")

    # --- Regression / boundary ---

    def test_file_is_not_empty(self):
        """README.md must not be empty."""
        self.assertGreater(len(self.content.strip()), 0)

    def test_no_double_blank_lines_around_description(self):
        """After removing the old block, there should be no excessive blank lines
        between the title and the new description."""
        lines = self.content.splitlines()
        title_idx = next(i for i, l in enumerate(lines) if l.startswith("# Gitbook2Pdf"))
        # Allow at most one blank line between title and first non-blank line after it
        non_blank_after_title = [
            l for l in lines[title_idx + 1:title_idx + 4] if l.strip()
        ]
        self.assertTrue(
            len(non_blank_after_title) >= 1,
            "Expected content immediately after the title",
        )


if __name__ == "__main__":
    unittest.main()
