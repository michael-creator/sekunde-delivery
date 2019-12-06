

from flask import render_template
from . import main
from .forms import ContactForm
from flask import render_template,request,redirect,url_for,abort
from ..models import  User


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


@main.route('/about', methods = ['GET','POST'])
def about():
    
    return render_template('about.html')

@main.route('/contact', methods = ['GET','POST'])
def profile():
    
    return render_template('contact.html')
@main.route('/services', methods = ["GET", "POST"])
def services():
    return render_template("services.html")
@main.route('/delivery', methods=['GET','POST'])
def delivery():
    return render_template("delivery.html")

@main.route('/checkout')

def checkout():
        return render_template('checkout.html')
    

