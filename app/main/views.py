from flask import Flask
from flask import render_template
from . import main
from flask_login import login_required


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
 
  