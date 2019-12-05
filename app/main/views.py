from flask import render_template
from . import main



@main.route('/')
def index():

    return render_template('index.html')

@main.route('/about', methods = ['GET','POST'])
def about():
    
    return render_template('about.html')

@main.route('/contact', methods = ['GET','POST'])
def profile():
    
    return render_template('contact.html')