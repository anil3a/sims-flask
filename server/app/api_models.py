from flask_restx import fields, Api
from app import db
from app.models import User, ActivityLog

def get_user_model(api: Api):
    return api.model('User', {
        'id': fields.Integer(description='The user ID'),
        'username': fields.String(required=True, description='The username'),
        'email': fields.String(required=True, description='The email address'),
        'password_hash': fields.String(description='The password hash'),
        'firstname': fields.String(description='The First name'),
        'lastname': fields.String(description='The Last name'),
    })

def get_item_model(api: Api):
    return api.model('Item', {
        'id': fields.Integer(description='The item ID'),
        'name': fields.String(required=True, description='The item name'),
        'quantity': fields.Integer(required=True, description='The item quantity')
    })

def get_new_item_model(api: Api):
    return api.model('ItemRequest', {
        'name': fields.String(required=True, description='The item name'),
        'quantity': fields.Integer(required=True, description='The item quantity')
    })

def get_login_model(api: Api):
    return api.model('Login', {
    'username': fields.String(required=True, description='The user username'),
    'password': fields.String(required=True, description='The user password')
})

def get_response_item_model(api: Api):
    return api.model('ItemResponse', {
        'message': fields.String,
        'item': fields.Nested(get_item_model(api)),
    })

def get_dashboard_activity_model(api: Api):
    return api.model('Activity', {
        'id': fields.Integer,
        'action': fields.String,
        'timestamp': fields.DateTime,
        'name': fields.String,
    })

def log_activity(user_id, action, rel_text=None, rel_id=None):
    user = User.query.filter_by(username=user_id).first()
    if not user:
        raise ValueError('User not found')

    activity_log = ActivityLog(user_id=user.id, action=action)

    if rel_text:
        activity_log.rel_text = rel_text
    if rel_id:
        activity_log.rel_id = rel_id

    db.session.add(activity_log)
    db.session.commit()
