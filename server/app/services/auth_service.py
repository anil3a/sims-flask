from flask import request
from app.models import User
from app import db
from flask_jwt_extended import create_access_token
from flask_restx import Namespace, Resource
from app.models import get_user_model
from app.utils.security import hash_password, check_password_hash, generate_access_token

auth_ns = Namespace('auth', description='Authentication related operations')

user_model = get_user_model(auth_ns)

@auth_ns.route('/register')
class RegisterService(Resource):
    @auth_ns.doc('user_model')
    @auth_ns.expect(user_model)
    def post(self):
        """Register a new user"""
        data = auth_ns.payload
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        firstname = data.get("firstname")
        lastname = data.get("lastname")

        if User.query.filter_by(username=username).first():
            return {'message': 'Username already exists'}, 400
        if User.query.filter_by(email=email).first():
            return {'message': 'Email already exists'}, 400

        password_hash = hash_password(password).decode('utf-8')
        new_user = User(
            username=username,
            email=email,
            password_hash=password_hash,
            firstname=firstname,
            lastname=lastname
        )
        db.session.add(new_user)
        db.session.commit()

        return {'message': 'User registered successfully'}, 201


@auth_ns.route('/login')
class LoginService(Resource):
    @auth_ns.doc('user_model')
    @auth_ns.expect(user_model)
    def post(self):
        """
        Log in an existing user.

        Expects a JSON object with 'username' and 'password'.
        """
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password_hash, password):
            access_token = generate_access_token(username)  # Example identity could be user.id
            return {'access_token': access_token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401
