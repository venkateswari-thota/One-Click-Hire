# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_cors import CORS

# # Initialize db and CORS
# db = SQLAlchemy()

# def create_app():
#     app = Flask(__name__)
#     CORS(app, origins=["http://localhost:3000"])

#     # Configuration
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yourdatabase.db'
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     app.config.from_object('config.Config')

#     # Initialize the database with the app
#     db.init_app(app)

#     # Register routes
#     from app.routes import main  # Import here to avoid circular import
#     app.register_blueprint(main, url_prefix='/api')

#     return app





from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
load_dotenv()  # This loads the .env file into the environment variables


db = SQLAlchemy()
mail = Mail()  # Initialize the mail object
bcrypt = Bcrypt()
jwt = JWTManager()
from flask import Flask

app = Flask(__name__)

@app.after_request
def add_no_cache_headers(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

def create_app():
    app = Flask(__name__)
    CORS(app, supports_credentials=True, origins=["http://localhost:3000","http://localhost:3001","https://atsresume-8ggeuqnly-asiya-tabasum-shaiks-projects.vercel.app"])
    # Configurations
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
    app.config['MAIL_SERVER'] = 'smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USERNAME'] = os.getenv('EMAIL_USER')
    app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_PASS')
    app.secret_key = "secret" 
    app.config["SECRET_KEY"] = "One_Click_Hire"
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET')
    app.config["SESSION_TYPE"] = "filesystem"
    app.config["SESSION_PERMANENT"] = True
    app.config["SESSION_USE_SIGNER"] = True
    app.config["UPLOAD_FOLDER"] = "uploads"

    print(os.getenv('EMAIL_USER'))
    print(os.getenv('EMAIL_PASS'))


    # Set the secret keys
    app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY','secret2')  # Flask secret key
    app.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY','secret')  # JWT secret key
    
    # Initialize extensions (e.g., CORS, JWTManager, Mail, etc.)
    from flask_jwt_extended import JWTManager
    JWTManager(app)

    # Initialize extensions
    db.init_app(app)
    mail.init_app(app)  # Initialize mail here
    bcrypt.init_app(app)
    jwt.init_app(app)
    
    with app.app_context():
        db.create_all()
    # Register blueprints
    from app.routes import main
    app.register_blueprint(main, url_prefix='/api')

    app.config["UPLOAD_FOLDER"] = "uploads"
    return app



