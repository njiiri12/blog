from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads,IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE



#create  instances.
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'
fa = FontAwesome()
photos = UploadSet('photos',IMAGES)
mail = Mail()
simple = SimpleMDE()

def create_app(config_name):

    app = Flask(__name__)

    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    app.config.from_object(config_options[config_name])
    
    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    fa.init_app(app)
    configure_uploads(app,photos)
    mail.init_app(app)
    simple.init_app(app)

    with app.app_context():
        

        db.create_all()

    # blueprints
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')
    

    # setting config
    from .request import configure_request
    configure_request(app)


    return app
