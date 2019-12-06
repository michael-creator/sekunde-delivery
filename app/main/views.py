from flask import render_template
from . import main
from .forms import ContactForm



@main.route('/')
def index():

    return render_template('index.html')


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

