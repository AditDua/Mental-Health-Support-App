from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///journal.db'
db = SQLAlchemy(app)

# Database model for users
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)

# Database model for journal entries
class JournalEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    mood = db.Column(db.Integer, nullable=False)
    entry = db.Column(db.Text, nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow)

# Helper to map moods to emojis
def get_mood_emoji(mood):
    emojis = {1: "😔", 2: "😕", 3: "😐", 4: "😊", 5: "😁"}
    return emojis.get(mood, "🙂")

@app.route('/')
def index():
    if 'username' not in session:
        return redirect(url_for('login'))

    user_id = session['user_id']
    entries = JournalEntry.query.filter_by(user_id=user_id).all()

    # Prepare data for the mood chart
    dates = [entry.date.strftime("%Y-%m-%d") for entry in entries]
    moods = [entry.mood for entry in entries]
    emojis = [get_mood_emoji(entry.mood) for entry in entries]

    return render_template('index.html', entries=entries, dates=dates, moods=moods, emojis=emojis)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['username'] = username
            session['user_id'] = user.id
            return redirect(url_for('index'))
        else:
            flash("Invalid username or password!", "danger")
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = generate_password_hash(request.form['password'])
        if User.query.filter_by(username=username).first():
            flash("Username already exists!", "danger")
            return redirect(url_for('register'))

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/journal', methods=['GET', 'POST'])
def add_journal():
    if 'username' not in session:
        return redirect(url_for('login'))

    if request.method == 'POST':
        mood = int(request.form['mood'])
        entry = request.form['entry']
        user_id = session['user_id']
        new_entry = JournalEntry(user_id=user_id, mood=mood, entry=entry)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('journal.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
