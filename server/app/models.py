from app import db
from flask_restx import fields, Api

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=True)

def get_user_model(api: Api):
    return api.model('User', {
        'id': fields.Integer(description='The user ID'),
        'username': fields.String(required=True, description='The username'),
        'email': fields.String(required=True, description='The email address'),
        'password_hash': fields.String(description='The password hash'),
        'firstname': fields.String(description='The First name'),
        'lastname': fields.String(description='The Last name'),
    })


class Item(db.Model):
    __tablename__ = 'item'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)


def get_item_model(api: Api):
    return api.model('Item', {
        'id': fields.Integer(description='The item ID'),
        'name': fields.String(required=True, description='The item name'),
        'quantity': fields.Integer(required=True, description='The item quantity')
    })
