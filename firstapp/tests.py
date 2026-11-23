from django.test import TestCase
from .forms import StudentForm


class StudentFormTests(TestCase):
    def test_mobile_is_available_in_cleaned_data(self):
        form = StudentForm({
            "name": "Ada",
            "email": "ada@example.com",
            "mobile": "5551234567",
            "age": "20",
        })

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data["mobile"], "5551234567")

    def test_registration_get_displays_form(self):
        response = self.client.get("/register/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Student Registration Form")

    def test_valid_registration_displays_mobile(self):
        response = self.client.post("/register/", {
            "name": "Ada",
            "email": "ada@example.com",
            "mobile": "5551234567",
            "age": "20",
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Mobile: 5551234567")

    def test_invalid_registration_retains_form_errors(self):
        response = self.client.post("/register/", {
            "name": "Ada",
            "email": "not-an-email",
            "mobile": "5551234567",
            "age": "20",
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Enter a valid email address.")
        self.assertContains(response, "5551234567")
