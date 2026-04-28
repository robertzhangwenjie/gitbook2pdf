"""
Tests for gitbook2pdf/libs/gitbook.css changes introduced in PR:
- Removed CSS block that forced page breaks between section.normal and h1 elements.
  Specifically removed:
    section.normal + section.normal,
    section.normal + h1,
    h1 + section.normal,
    h1 + h1 {
      page-break-before: always;
      break-before: page;
    }
"""
import os
import re
import unittest

CSS_PATH = os.path.join(
    os.path.dirname(__file__), "..", "gitbook2pdf", "libs", "gitbook.css"
)


class TestGitbookCssPageBreakRemoval(unittest.TestCase):
    def setUp(self):
        with open(CSS_PATH, encoding="utf-8") as f:
            self.content = f.read()

    # --- Removed selectors must be absent ---

    def test_removed_selector_section_plus_section(self):
        """'section.normal + section.normal' selector must be removed."""
        self.assertNotIn("section.normal + section.normal", self.content)

    def test_removed_selector_section_plus_h1(self):
        """'section.normal + h1' adjacent sibling selector must be removed."""
        self.assertNotIn("section.normal + h1", self.content)

    def test_removed_selector_h1_plus_section(self):
        """'h1 + section.normal' adjacent sibling selector must be removed."""
        self.assertNotIn("h1 + section.normal", self.content)

    def test_removed_selector_h1_plus_h1(self):
        """'h1 + h1' adjacent sibling selector must be removed."""
        self.assertNotIn("h1 + h1", self.content)

    # --- Removed properties must not appear in the now-deleted rule block ---

    def test_no_page_break_before_always_for_removed_selectors(self):
        """page-break-before: always must not be associated with the removed selectors.

        The property itself may legitimately appear elsewhere in the file for
        other rules, so we target the removed comment block specifically.
        """
        self.assertNotIn("Make each chapter start on a new page in the PDF output", self.content)

    def test_removed_break_before_page_property_context(self):
        """break-before: page combined in the removed rule block should be absent.

        We verify the removed comment that surrounded the block is gone,
        since break-before: page could appear in other valid contexts.
        """
        # The comment was the unique identifier of the deleted block
        self.assertNotIn("Make each chapter start on a new page", self.content)

    def test_break_before_page_not_present(self):
        """break-before: page should not appear anywhere — it was only used in the removed block."""
        # In the original file this property appeared only inside the removed block.
        self.assertNotIn("break-before: page", self.content)

    def test_page_break_before_always_not_present(self):
        """page-break-before: always should not appear anywhere — it was only in the removed block."""
        self.assertNotIn("page-break-before: always", self.content)

    # --- File integrity after the removal ---

    def test_file_is_not_empty(self):
        """CSS file must not be empty after the removal."""
        self.assertGreater(len(self.content.strip()), 0)

    def test_file_ends_properly(self):
        """CSS file should end with a closing brace and optional whitespace."""
        stripped = self.content.rstrip()
        self.assertTrue(
            stripped.endswith("}"),
            f"Expected file to end with '}}', got: {stripped[-20:]!r}",
        )

    def test_last_rule_is_opacity_rule(self):
        """After the page-break block is removed, the last rule should be the
        opacity: 0.5 declaration for .xml .hljs-cdata."""
        # Find the last occurrence of 'opacity: 0.5'
        last_opacity = self.content.rfind("opacity: 0.5")
        last_brace = self.content.rfind("}")
        # The last closing brace should come after the last opacity declaration
        self.assertGreater(last_brace, last_opacity)
        # And there should be no selectors after the last opacity rule's closing brace
        content_after_last_brace = self.content[last_brace + 1:].strip()
        self.assertEqual(
            content_after_last_brace,
            "",
            "No CSS rules should follow the last closing brace",
        )

    def test_hljs_cdata_rule_still_present(self):
        """The .xml .hljs-cdata rule directly above the removed block must still exist."""
        self.assertIn(".xml .hljs-cdata", self.content)

    def test_color_theme_2_rules_intact(self):
        """color-theme-2 rules that precede the removed block must still be intact."""
        self.assertIn(".book.color-theme-2", self.content)

    # --- Regression: ensure no accidental removal of unrelated page-break usage ---

    def test_no_adjacent_sibling_selectors_for_section_or_h1(self):
        """No adjacent-sibling combinator rules targeting section.normal or bare h1 remain."""
        # Pattern: any rule using '+' combinator with section.normal or h1 for page breaks
        pattern = re.compile(
            r"(section\.normal\s*\+\s*(section\.normal|h1))|(h1\s*\+\s*(section\.normal|h1))"
        )
        self.assertIsNone(
            pattern.search(self.content),
            "Found unexpected adjacent-sibling selector involving section.normal or h1",
        )


if __name__ == "__main__":
    unittest.main()