from flask import render_template
from . import main
from forms import ContactForm



@main.route('/')
def index():

    return render_template('index.html')