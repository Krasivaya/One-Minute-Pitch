from flask import Flask
from flask_bootstrap import Bootstrap
from config import configurations
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail

app = Flask(__name__)
bootstrap = Bootstrap()
db = SQLAlchemy()

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

photos = UploadSet('photos',IMAGES)
mail = Mail()

def create_app(configname):

    # Creating the app configurations
    app.config.from_object(configurations[configname])

    # Registering the blueprint
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    
    
    # configure UploadSet
    configure_uploads(app,photos)

    return app