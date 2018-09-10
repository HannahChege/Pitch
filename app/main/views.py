from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Pitch,Comment,Like,Dislike
from flask_login import login_required, current_user
from .forms import PitchForm,UpdateProfile
from .. import db,photos


# Views
@main.route('/Pickupline', methods=['GET','POST'])
@login_required
def Pickupline():
   pitch_form=PitchForm()
   if pitch_form.validate_on_submit():

       Pickupline = Pitch(category=pitch_form.category.data,title = pitch_form.title.data)
       db.session.add(Pickupline)
       db.session.commit()
   Pickupline = Pitch.query.filter_by(category='Pickupline').all()
   return render_template('Pickupline.html',Pickupline=Pickupline,pitch_form=pitch_form)


@main.route('/')
def index():
    '''
    View the root page function
    '''
    title = "Pitches"
    return render_template('index.html', title = title)

@main.route('/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    pitch = get_pitch(id)
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data

        # Updated review instance
        new_pitch = Pitch(pitch_id=pitch.id,pitch_title=title,image_path=movie.poster,movie_review=review,user=current_user)

        # save review method
        new_pitch.save_pitch()
        return redirect(url_for('.pitch',id = pitch.id ))

    title = f'{pitch.title} review'
    return render_template('new_pitch.html',title = title, pitch_form=form, pitch=pitch)

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
 
  