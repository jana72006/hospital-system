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

## Publishing

This project includes a Render Blueprint in `render.yaml`. To publish the interactive app:

1. [Deploy this project to Render](https://render.com/deploy?repo=https://github.com/jana72006/hospital-system) and sign in or connect your GitHub account if asked.
2. Select **New > Blueprint** and choose `jana72006/hospital-system`.
3. Review the `hospital-system` free web service and select **Apply** to create and deploy it.
4. Once the first deploy succeeds, open its `onrender.com` address. Later pushes to `main` deploy automatically.

The Blueprint creates a private `SECRET_KEY` automatically. The free instance can spin down when idle, so the first visit may take about a minute. GitHub Pages cannot run the Python backend.

## Project structure

```text
app.py
templates/
  index.html
static/
  styles.css
requirements.txt
tests/
  test_app.py
```
