from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return f'<Note {self.id}>'

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    notes = Note.query.order_by(Note.created_at.desc()).all()
    return render_template('index.html', notes=notes)

@app.route('/notes', methods=['POST'])
def add_note():
    content = request.form.get('content')
    if content:
        note = Note(content=content)
        db.session.add(note)
        db.session.commit()
    return render_template('partials/note.html', note=note)

@app.route('/notes/<int:id>', methods=['GET'])
def get_note(id):
    note = Note.query.get_or_404(id)
    return render_template('partials/note.html', note=note)

@app.route('/notes/<int:id>/edit', methods=['GET'])
def edit_note(id):
    note = Note.query.get_or_404(id)
    return render_template('partials/note_form.html', note=note)

@app.route('/notes/<int:id>', methods=['PUT', 'POST'])
def update_note(id):
    note = Note.query.get_or_404(id)
    note.content = request.form.get('content')
    db.session.commit()
    return render_template('partials/note.html', note=note)

@app.route('/notes/<int:id>', methods=['DELETE', 'POST'])
def delete_note(id):
    note = Note.query.get_or_404(id)
    db.session.delete(note)
    db.session.commit()
    return ""

if __name__ == '__main__':
    app.run(debug=True)
