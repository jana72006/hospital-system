# Nile Hospital

A polished, responsive hospital website built with Python and Flask as a student project. It brings the original desktop project's main ideas—doctor profiles, appointment requests, a pharmacy, skincare, and an about section—into a single web experience.

## Run locally

1. Install Python 3.10 or newer.
2. Create and activate a virtual environment:

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

3. Install dependencies and start the app:

   ```powershell
   pip install -r requirements.txt
   python app.py
   ```

4. Open <http://127.0.0.1:5000>.

## Tests

Run the automated checks from the project directory:

```powershell
python -m unittest discover -s tests -v
```

## Demo behavior

- Appointment and pharmacy forms validate their selections and show a confirmation.
- Requests are examples only: no real appointment is booked, no order is placed, and no personal or patient information is collected or stored.
- The doctor directory, products, prices, and availability are illustrative project content—not medical advice or a live hospital service.
- The secret key is generated for local development. Set a private `SECRET_KEY` environment variable when deploying the app.

## View the website online

GitHub Pages publishes a public website automatically whenever changes are pushed to `main`. The address is:

<https://jana72006.github.io/hospital-system/>

The GitHub Actions workflow renders `templates/index.html` with the Flask app and copies `static/styles.css` using the Python script `build_pages.py`. Python remains the source of truth for the website's doctors, products, availability, and pages. No Render, extra hosting account, build command, or local server is needed to view the online site.

The repository is configured to publish through **GitHub Actions**. The first publication can take a few minutes; check the **Actions** tab if you want to follow its progress. Every later push to `main` publishes the latest version automatically.

The hosted pages site is static: appointment and pharmacy requests display demo confirmations in the browser, but do not reach the Flask server or book, send, or save anything. To run the full Flask app and its Python form handlers locally, follow the steps above.

## Project structure

```

To preview the standalone Pages version locally:

```powershell
python build_pages.py
python -m http.server 8000 --directory site
```

Then open <http://127.0.0.1:8000>. Close the preview with Ctrl+C.text
app.py
templates/
  index.html
static/
  styles.css
requirements.txt
tests/
  test_app.py
  test_static_site.py
build_pages.py
site/
.github/
  workflows/
    deploy-pages.yml
```
