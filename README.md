# Python Web Development with Flask

Small Flask notes app with authentication and SQLite storage.

## Setup

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run

```powershell
python main.py
```

The app creates `website/database.db` automatically on first start.

## Test

```powershell
python -m unittest discover -s tests -v
```

## Demo Checklist

Use this flow for a quick submission demo:

1. Start the app with `python main.py`.
2. Open the site and show the login and sign-up pages.
3. Create a new account and point out the success message.
4. Add two notes and show the timestamp on each one.
5. Delete one note and show that the other remains.
6. Log out and show that the home page redirects back to login.
7. Log back in and show that the saved note is still attached to that account.

## Demo Files

Put your recorded demo in the `demo/` folder before submission if you want the video saved alongside the project files.
