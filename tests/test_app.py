import unittest

from app import APPOINTMENT_DAYS, APPOINTMENT_TIMES, DOCTORS, PHARMACY_PRODUCTS, app


class HospitalWebsiteTests(unittest.TestCase):
    def setUp(self):
        app.config.update(TESTING=True, SECRET_KEY="test-secret")
        self.client = app.test_client()

    def csrf_token(self):
        self.client.get("/")
        with self.client.session_transaction() as browser_session:
            return browser_session["_csrf_token"]

    def test_homepage_renders_main_sections_and_project_notice(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        page = response.get_data(as_text=True)
        for section in ("Our care", "Our doctors", "Pharmacy", "Request a visit"):
            self.assertIn(section, page)
        self.assertIn("This website is a learning project.", page)

    def test_appointment_request_confirms_demo_without_saving_it(self):
        response = self.client.post(
            "/appointments",
            data={
                "csrf_token": self.csrf_token(),
                "doctor": DOCTORS[0]["id"],
                "date": APPOINTMENT_DAYS[0].isoformat(),
                "time": APPOINTMENT_TIMES[0],
            },
        )

        self.assertEqual(response.status_code, 302)
        page = self.client.get(response.headers["Location"]).get_data(as_text=True)
        self.assertIn("No appointment was booked or saved.", page)

    def test_invalid_appointment_selection_is_rejected(self):
        response = self.client.post(
            "/appointments",
            data={
                "csrf_token": self.csrf_token(),
                "doctor": "not-a-doctor",
                "date": "2024-01-01",
                "time": "11:11 AM",
            },
        )

        page = self.client.get(response.headers["Location"]).get_data(as_text=True)
        self.assertIn("Please choose a doctor and an available date and time.", page)

    def test_pharmacy_request_validates_quantity(self):
        response = self.client.post(
            "/pharmacy",
            data={
                "csrf_token": self.csrf_token(),
                "product": PHARMACY_PRODUCTS[0]["id"],
                "quantity": "11",
            },
        )

        page = self.client.get(response.headers["Location"]).get_data(as_text=True)
        self.assertIn("Please choose an item and a quantity from 1 to 10.", page)

    def test_post_without_csrf_token_is_rejected(self):
        response = self.client.post("/pharmacy", data={"product": "aspirin", "quantity": "1"})

        self.assertEqual(response.status_code, 400)
        self.assertIn(b"form expired", response.data)


if __name__ == "__main__":
    unittest.main()
