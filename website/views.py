from flask import Blueprint, render_template
from .models import User, Event
from . import db
from os import path

views = Blueprint('views', __name__)

@views.route('/')
def home():
    # try:
    #     admin_one = User(username='markvschultheis', password='Admin1')
    #     db.session.add(admin_one)
    #     # new_event = Event(
    #     #     title='Test',
    #     #     description='This is a test',
    #     #     link='https://ajajajaja.com',
    #     #     location='501 Westgate Rd'
    #     # )
    #     # db.session.add(new_event)
    #     # new_event1 = Event(
    #     #     title='Test1',
    #     #     description='This is a test1',
    #     #     link='https://ajajajaja1.com',
    #     #     location='501 Westgate Rd'
    #     # )
    #     # db.session.add(new_event1)
    #     db.session.commit()
    # except Exception as e:
    #     print(e)
    events = Event.query.all()
    return render_template('index.html', event_list=events)

@views.route('/bio')
def bio():
    return render_template('bio.html')

@views.route('/support')
def support():
    return render_template('support.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

@views.route('/awards')
def awards():
    return render_template('awards.html')

@views.route('/media')
def media():
    return render_template('media.html')

@views.route('/lessons')
def lessons():
    return render_template('lessons.html')
    