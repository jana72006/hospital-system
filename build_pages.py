from __future__ import annotations

import re
import shutil
from pathlib import Path

from app import PHARMACY_PRODUCTS, app

PROJECT_ROOT = Path(__file__).parent
SITE_DIRECTORY = PROJECT_ROOT / "site"


def build_site(output_directory: Path = SITE_DIRECTORY) -> Path:
    response = app.test_client().get("/")
    if response.status_code != 200:
        raise RuntimeError(f"Flask homepage returned HTTP {response.status_code}.")
    html = response.get_data(as_text=True)

    appointment_form = '<form class="appointment-form" method="post" action="/appointments">'
    static_appointment_form = (
        '<form class="appointment-form" data-pages-demo="appointment" '
        'method="post" action="#">'
    )
    if html.count(appointment_form) != 1:
        raise RuntimeError("Expected exactly one appointment form in the Flask homepage.")
    html = html.replace(appointment_form, static_appointment_form, 1)

    pharmacy_form = '<form method="post" action="/pharmacy">'
    if html.count(pharmacy_form) != len(PHARMACY_PRODUCTS):
        raise RuntimeError("Pharmacy forms do not match the Flask product catalog.")
    html = html.replace(
        pharmacy_form,
        '<form data-pages-demo="pharmacy" method="post" action="#">',
    )

    html = re.sub(r'\s*<input type="hidden" name="csrf_token" value="[^"]*">', "", html)
    html = html.replace('href="/static/', 'href="static/')

    output_directory.mkdir(parents=True, exist_ok=True)
    (output_directory / "index.html").write_text(html, encoding="utf-8")
    (output_directory / "404.html").write_text(html, encoding="utf-8")

    static_directory = output_directory / "static"
    if static_directory.exists():
        shutil.rmtree(static_directory)
    shutil.copytree(PROJECT_ROOT / "static", static_directory)

    return output_directory


if __name__ == "__main__":
    print(f"Built GitHub Pages website in {build_site()}")
