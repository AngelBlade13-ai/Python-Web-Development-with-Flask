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


## Demo Video

https://github.com/user-attachments/assets/9bbdb5c1-7083-48e5-a3ee-307a9b6282a7

If the embedded preview does not show the full recording on GitHub, use the direct full demo link below:

Full demo link: https://github.com/user-attachments/assets/9bbdb5c1-7083-48e5-a3ee-307a9b6282a7
