from flask import Blueprint, render_template, request, flash, jsonify, redirect
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/dp', methods=['GET', 'POST'])
@login_required
def dp():
    return render_template("dp.html", user=current_user)

@views.route('/sp', methods=['GET', 'POST'])
@login_required
def sp():
    return render_template("sp.html", user=current_user)

@views.route('/op', methods=['GET', 'POST'])
@login_required
def op():
    return render_template("op.html", user=current_user)

@views.route('/videos', methods=['GET', 'POST'])
@login_required
def videos():
    return render_template("videos.html", user=current_user)

@views.route('/notes', methods=['GET', 'POST'])
@login_required
def notes():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("notes.html", user=current_user)



@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            return redirect(url_for('views.notes'))

    return jsonify({})