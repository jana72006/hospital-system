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

## Demo behavior

- Appointment and pharmacy forms validate their selections and show a confirmation.
- Requests are examples only: no real appointment is booked, no order is placed, and no personal or patient information is collected or stored.
- The doctor directory, products, prices, and availability are illustrative project content—not medical advice or a live hospital service.
- The secret key is generated for local development. Set a private `SECRET_KEY` environment variable when deploying the app.

## Publishing

This repository contains a Python Flask application. GitHub Pages serves static websites and cannot run its Python backend; deploy the app to a Python host such as Render or Railway to make the interactive site public, then link that deployment from this repository.

## Project structure

```text
app.py
templates/
  index.html
static/
  styles.css
requirements.txt
```
