from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Event
from . import db

admin = Blueprint('admin', __name__)

@admin.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        user = User.query.filter_by(username=username).first()
        if user:
            if user.password == password or check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('admin.dashboard'))
    return render_template('admin.html')

@admin.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    if request.method == 'POST':
        form_type = request.form.get('formtype')
        if form_type == 'event':
            new_event = Event(
                title = request.form.get('title'),
                description = request.form.get('description'),
                link = request.form.get('link'),
                date = request.form.get('date'),
                location = request.form.get('location')
            )
            db.session.add(new_event)
            db.session.commit()
        elif form_type == 'delevent':
            event_id = request.form.get('eventid')
            event = Event.query.get(event_id)
            if event:
                db.session.delete(event)
                db.session.commit()
        elif form_type == 'user':
            username = request.form.get('username')
            user = User.query.filter_by(username=username).first()
            if not user:
                password = request.form.get('user_password')
                password_test = request.form.get('user_password_check')
                if password == password_test:
                    new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
                    db.session.add(new_user)
                    db.session.commit()
        elif form_type == 'deluser':
            user_id = request.form.get('userid')
            user = User.query.get(user_id)
            if user and (user.username != 'markvschultheis'):
                db.session.delete(user)
                db.session.commit()
                
    events = Event.query.all()
    users = User.query.all()
    return render_template('dashboard.html', event_list=events, user_list=users)