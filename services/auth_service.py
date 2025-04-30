from models.user import User
from extensions import db, bcrypt
from flask_jwt_extended import create_access_token

class AuthService:
    @staticmethod
    def register(email: str, password: str):
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return None, 'Email already registered.'

        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(email=email, password_hash=hashed_pw)
        db.session.add(user)
        db.session.commit()

        return user, None

    @staticmethod
    def login(email: str, password: str):
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password_hash, password):
            token = create_access_token(identity=str(user.id))
            return token, None
        return None, 'Invalid email or password.'

