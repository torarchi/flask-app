from flask import Flask
from config import Config
from extensions import db, bcrypt, jwt
from flasgger import Swagger
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    
    CORS(app, origins=[r"http://localhost:\d+", r"http://127.0.0.1:\d+"], supports_credentials=True)
    
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    Swagger(app)

    from controllers.auth_controller import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/api/auth')

    with app.app_context():
        db.create_all()

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

