from flask import Blueprint, flash, jsonify, render_template, request
from flask_login import current_user, login_required

from . import db
from .models import Note


views = Blueprint("views", __name__)


@views.route("/", methods=["GET", "POST"])
@login_required
def home():
    if request.method == "POST":
        note = (request.form.get("note") or "").strip()

        if not note:
            flash("Note is too short!", category="error")
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash("Note added!", category="success")

    return render_template("home.html", user=current_user)


@views.route("/delete-note", methods=["POST"])
@login_required
def delete_note():
    note_data = request.get_json(silent=True) or {}
    note_id = note_data.get("noteId")

    try:
        note_id = int(note_id)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid note id."}), 400

    note = db.session.get(Note, note_id)

    if note is None:
        return jsonify({"error": "Note not found."}), 404

    if note.user_id != current_user.id:
        return jsonify({"error": "Forbidden."}), 403

    db.session.delete(note)
    db.session.commit()

    return jsonify({"success": True})
