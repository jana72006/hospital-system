from __future__ import annotations

import hmac
import os
import secrets
from datetime import date, timedelta

from flask import Flask, abort, flash, redirect, render_template, request, session, url_for

app = Flask(__name__)
app.config.update(
    SECRET_KEY=os.environ.get("SECRET_KEY") or secrets.token_hex(32),
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

DOCTORS = [
    {"id": "mustafa-anwar", "name": "Dr. Mustafa Anwar", "specialty": "Dentistry", "icon": "✦"},
    {"id": "ahmed-ashour", "name": "Dr. Ahmed Ashour", "specialty": "General Surgery", "icon": "＋"},
    {"id": "ahmed-sultan", "name": "Dr. Ahmed Sultan", "specialty": "Chest & Allergy", "icon": "♡"},
    {"id": "omar-el-banhawy", "name": "Dr. Omar El Banhawy", "specialty": "ENT", "icon": "◉"},
    {"id": "rami-ramzy", "name": "Dr. Rami Ahmed Ramzy", "specialty": "Therapeutic Nutrition", "icon": "❋"},
    {"id": "ahmed-mahdi", "name": "Dr. Ahmed Essam Mahdi", "specialty": "Neurology", "icon": "✧"},
    {"id": "hager-aref", "name": "Dr. Hager Aref", "specialty": "General Surgery", "icon": "✿"},
    {"id": "alaa-hajjaj", "name": "Dr. Alaa Hajjaj", "specialty": "Dermatology", "icon": "❀"},
]

PHARMACY_PRODUCTS = [
    {"id": "aspirin", "name": "Aspirin 500mg", "category": "Everyday care", "price": "$5.00", "icon": "💊", "color": "mint"},
    {"id": "paracetamol", "name": "Paracetamol 650mg", "category": "Pain relief", "price": "$3.00", "icon": "🩹", "color": "peach"},
    {"id": "ibuprofen", "name": "Ibuprofen 200mg", "category": "Pain relief", "price": "$4.00", "icon": "💊", "color": "lilac"},
    {"id": "listerine", "name": "Listerine", "category": "Oral care", "price": "$6.00", "icon": "🫧", "color": "sky"},
]

BEAUTY_PRODUCTS = [
    {"name": "Daily Moisturizer", "category": "Hydration", "price": "$12.00", "icon": "🧴", "color": "peach"},
    {"name": "Face Serum", "category": "Skin essentials", "price": "$18.00", "icon": "✨", "color": "lilac"},
    {"name": "Everyday Sunscreen", "category": "Sun care", "price": "$15.00", "icon": "☀", "color": "mint"},
    {"name": "Gentle Face Wash", "category": "Cleanse", "price": "$9.00", "icon": "🫧", "color": "sky"},
]

APPOINTMENT_DAYS = [
    date.today() + timedelta(days=offset)
    for offset in range(1, 8)
    if (date.today() + timedelta(days=offset)).weekday() != 4
]
APPOINTMENT_TIMES = ["09:00 AM", "10:30 AM", "12:00 PM", "02:30 PM"]


@app.context_processor
def inject_template_helpers() -> dict[str, object]:
    def csrf_token() -> str:
        token = session.get("_csrf_token")
        if token is None:
            token = secrets.token_urlsafe(32)
            session["_csrf_token"] = token
        return token

    return {"csrf_token": csrf_token}


@app.before_request
def protect_demo_forms() -> None:
    if request.method == "POST":
        expected = session.get("_csrf_token", "")
        supplied = request.form.get("csrf_token", "")
        if not expected or not hmac.compare_digest(expected, supplied):
            abort(400, description="This form expired. Refresh the page and try again.")


@app.get("/")
def home():
    return render_template(
        "index.html",
        doctors=DOCTORS,
        pharmacy_products=PHARMACY_PRODUCTS,
        beauty_products=BEAUTY_PRODUCTS,
        appointment_days=APPOINTMENT_DAYS,
        appointment_times=APPOINTMENT_TIMES,
        today=date.today(),
    )


@app.post("/appointments")
def request_appointment():
    doctor = next(
        (item for item in DOCTORS if item["id"] == request.form.get("doctor")),
        None,
    )
    try:
        appointment_day = date.fromisoformat(request.form.get("date", ""))
    except ValueError:
        appointment_day = None

    appointment_time = request.form.get("time", "")
    if (
        doctor is None
        or appointment_day not in APPOINTMENT_DAYS
        or appointment_time not in APPOINTMENT_TIMES
    ):
        flash("Please choose a doctor and an available date and time.", "error")
    else:
        flash(
            f"Demo request received for {doctor['name']} on "
            f"{appointment_day.strftime('%B %d')} at {appointment_time}. "
            "No appointment was booked or saved.",
            "success",
        )
    return redirect(url_for("home", _anchor="appointments"))


@app.post("/pharmacy")
def request_product():
    product = next(
        (item for item in PHARMACY_PRODUCTS if item["id"] == request.form.get("product")),
        None,
    )
    try:
        quantity = int(request.form.get("quantity", "1"))
    except ValueError:
        quantity = 0

    if product is None or not 1 <= quantity <= 10:
        flash("Please choose an item and a quantity from 1 to 10.", "error")
    else:
        flash(
            f"Demo request received for {quantity} × {product['name']}. "
            "No order was placed or saved.",
            "success",
        )
    return redirect(url_for("home", _anchor="pharmacy"))


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=int(os.environ.get("PORT", "5000")),
        debug=os.environ.get("FLASK_DEBUG") == "1",
    )
