import unittest
import os


class TestHTMLOutput(unittest.TestCase):
    def test_html_sample_exists(self):
        """Confirm the HTML sample report exists in the docs folder."""
        self.assertTrue(
            os.path.exists("docs/sample_weekly_operating_review.html"),
            "docs/sample_weekly_operating_review.html should exist"
        )

    def test_md_sample_still_exists(self):
        """Confirm the original Markdown sample was not removed."""
        self.assertTrue(
            os.path.exists("docs/sample_weekly_operating_review.md"),
            "docs/sample_weekly_operating_review.md should still exist"
        )


if __name__ == "__main__":
    unittest.main()
