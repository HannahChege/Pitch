from flask import Flask
from flask import render_template,redirect,url_for
from . import main
from flask_login import login_required
from .forms import PitchForm
from .. models import User,Pitch,Comment,Like,Dislike
from ..import db


@main.route('/')
def index():
    pitches = Pitch.query.all()
    '''
    View the root page function
    '''
    title = "Pitches"
    return render_template('index.html', title = title,pitches=pitches)

@main.route('/new/pitch', methods = ['GET','POST'])
@login_required
def new_pitch():
    formpitch = PitchForm()
    if formpitch.validate_on_submit():
        pitch = Pitch(category = formpitch.category.data, content = formpitch.pitch.data)
        db.session.add(pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
     
    return render_template('pitch.html',formpitch = formpitch)   

@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):  
    '''
    View the root page function
    ''' 


@main.route('/upvote/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_upvote(pitch_id):
    '''
    View the root page function
    '''     

@main.route('/downvote/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_downvote(pitch_id): 
    '''
    View the root page function
    '''
 
  