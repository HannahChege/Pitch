from flask import Flask
from flask import render_template,request,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User
from .forms import forms,UpdateProfile
from .. import db,photos


# Views
@main.route('/')
def index():
    '''
    View the root page function
    '''
    title = "Pitches"
    return render_template('index.html', title = title)

@main.route('/new/pitch', methods = ['GET','POST'])
@login_required
def new_pitch(pitch_id):
    '''
    View the root page function
    '''    

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
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
  