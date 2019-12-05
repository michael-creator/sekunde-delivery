from flask import render_template
from . import main
from .forms import ContactForm
from flask import render_template,request,redirect,url_for,abort
from ..models import Reviews, User



@main.route('/')
def index():

    return render_template('index.html')

@main.route('/sekunde-delivery/new/<int:id>', methods = ['GET','POST'])
def contact():
    form = ContactForm()
    return render_template('contact.html', form=form) 

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
