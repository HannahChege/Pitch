from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required


class PitchForm(FlaskForm):
    category=SelectField('category',
       choices=[('inspiration', 'inspiration'), ('pickuplines', 'pickuplines'), ('technoloy', 'technoloy'),
        ('411', '411')], validators = [Required()])
    pitch = TextAreaField('Pitch')
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio= TextAreaField('Tell us about you.', validators=[Required()])
    submit= SubmitField('Submit')