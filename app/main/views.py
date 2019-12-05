from flask import render_template
from . import main
from .forms import ContactForm

@main.route('/')
def index():

    return render_template('index.html')

@main.route('/sekunde-delivery/new/<int:id>', methods = ['GET','POST'])
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form) git