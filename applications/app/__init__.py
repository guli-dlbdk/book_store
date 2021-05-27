from flask import (Flask, render_template, session, redirect)
from flask_session import Session
from app.api.user import api_bp as user_api_bp
from app.api.book import api_bp as book_api_bp
from config import SESSION_LIFETIME
from datetime import timedelta



app = Flask(__name__,
            static_url_path='/static',
            static_folder='static')
app.config.from_object('config')



Session(app)

app.register_blueprint(user_api_bp)
app.register_blueprint(book_api_bp)

app.permanent_session_lifetime = timedelta(seconds=SESSION_LIFETIME)


@app.route('/')
def index():
    if not session.get('user_id'):
        return redirect('/login')
    session.permanent = True
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    if session.get('role') == 'admin':
        return redirect('/profiles')
    return render_template('profile.html')

@app.route('/profiles')
def profiles():
    if session.get('role') != 'admin':
        return redirect('/profile')
    return render_template('profiles.html')