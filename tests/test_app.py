import unittest

from werkzeug.security import generate_password_hash

from website import create_app, db
from website.models import Note, User


class FlaskAppTests(unittest.TestCase):
    def setUp(self):
        self.app = create_app(
            {
                "TESTING": True,
                "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",
                "SECRET_KEY": "test-secret",
            }
        )
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.drop_all()
        db.create_all()
        self.client = self.app.test_client()

    def tearDown(self):
        engine = db.engine
        db.session.remove()
        db.drop_all()
        engine.dispose()
        self.app_context.pop()

    def sign_up(self, email="test@example.com", first_name="Test", password="password123"):
        return self.client.post(
            "/sign-up",
            data={
                "email": email,
                "firstName": first_name,
                "password1": password,
                "password2": password,
            },
            follow_redirects=True,
        )

    def login(self, email="test@example.com", password="password123"):
        return self.client.post(
            "/login",
            data={"email": email, "password": password},
            follow_redirects=True,
        )

    def test_home_redirects_anonymous_users_to_login(self):
        response = self.client.get("/", follow_redirects=False)

        self.assertEqual(response.status_code, 302)
        self.assertIn("/login", response.headers["Location"])

    def test_sign_up_logs_user_in_and_creates_account(self):
        response = self.sign_up()

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Account created!", response.data)
        self.assertEqual(User.query.count(), 1)

    def test_blank_note_is_rejected(self):
        self.sign_up()
        response = self.client.post("/", data={"note": "   "}, follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Note is too short!", response.data)
        self.assertEqual(Note.query.count(), 0)

    def test_delete_note_requires_owned_note(self):
        owner = User(
            email="owner@example.com",
            first_name="Owner",
            password=generate_password_hash("password123"),
        )
        other_user = User(
            email="other@example.com",
            first_name="Other",
            password=generate_password_hash("password123"),
        )
        db.session.add_all([owner, other_user])
        db.session.commit()

        note = Note(data="private", user_id=other_user.id)
        db.session.add(note)
        db.session.commit()

        self.login(email="owner@example.com")
        response = self.client.post("/delete-note", json={"noteId": note.id})

        self.assertEqual(response.status_code, 403)
        self.assertEqual(Note.query.count(), 1)

    def test_delete_note_rejects_invalid_payload(self):
        self.sign_up()
        response = self.client.post("/delete-note", json={"noteId": "abc"})

        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
