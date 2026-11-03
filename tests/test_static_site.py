import tempfile
import unittest
from pathlib import Path

from build_pages import PROJECT_ROOT, build_site


class StaticSiteBuildTests(unittest.TestCase):
    def test_build_exports_the_flask_homepage_and_styles(self):
        with tempfile.TemporaryDirectory() as directory:
            output = build_site(Path(directory) / "site")

            page = (output / "index.html").read_text(encoding="utf-8")
            self.assertIn("Nile Hospital | Care, made personal", page)
            self.assertIn('href="static/styles.css"', page)
            self.assertTrue((output / "static" / "styles.css").is_file())
            self.assertEqual(
                (output / "static" / "styles.css").read_bytes(),
                (PROJECT_ROOT / "static" / "styles.css").read_bytes(),
            )
            self.assertTrue((output / "404.html").is_file())

    def test_static_forms_work_without_a_flask_server(self):
        with tempfile.TemporaryDirectory() as directory:
            output = build_site(Path(directory) / "site")
            page = (output / "index.html").read_text(encoding="utf-8")

            self.assertIn('data-pages-demo="appointment" method="post" action="#"', page)
            self.assertEqual(page.count('data-pages-demo="pharmacy" method="post" action="#"'), 4)
            self.assertNotIn('name="csrf_token"', page)
            self.assertNotIn('action="/appointments"', page)
            self.assertNotIn('action="/pharmacy"', page)
            self.assertIn('querySelectorAll("form[data-pages-demo]")', page)
            self.assertNotIn("{{", page)
            self.assertNotIn("{%", page)


if __name__ == "__main__":
    unittest.main()
