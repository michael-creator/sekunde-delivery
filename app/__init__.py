from flask import Flask
from config import config_options




from flask_login import LoginManager
from flask_bootstrap import Bootstrap

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'


def create_app(config_name):

    app=Flask(__name__)
    app.config.from_object(config_options[config_name])

    

    bootstrap = Bootstrap(app)
    login_manager.init_app(app)
    #....
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    
    return app