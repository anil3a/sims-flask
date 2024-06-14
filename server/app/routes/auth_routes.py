from flask import request
from app.services.auth_service import user_model, Register, Login
from flask_restx import Resource, Namespace, fields
from app.models import get_user_model


auth_ns = Namespace('auth', description='Authentication related operations')


# Register the user_model with the namespace
user_model = get_user_model(auth_ns)


auth_ns.add_resource(Register, '/register')
auth_ns.add_resource(Login, '/login')
