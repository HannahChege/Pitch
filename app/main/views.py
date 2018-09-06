from flask import render_template
from . import main


# Views
@main.route('/')
def index():
    '''
    View the root page function
    '''
    title = "Pitches"
    return render_template('index.html', title = title)