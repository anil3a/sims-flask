from app import db

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    firstname = db.Column(db.String(64), nullable=False)
    lastname = db.Column(db.String(64), nullable=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password


class Item(db.Model):
    __tablename__ = 'item'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity


class ActivityLog(db.Model):
    __tablename__ = 'activitylog'
    
    id = db.Column(db.Integer, primary_key=True)
    action = db.Column(db.String(128), nullable=False)
    timestamp = db.Column(db.DateTime, default=db.func.current_timestamp())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('activities', lazy=True))
    rel_text = db.Column(db.String(64), nullable=True)
    rel_id = db.Column(db.Integer, nullable=True)

    def __init__(self, action, user_id, rel_text=None, rel_id=None):
        self.action = action
        self.user_id = user_id
        self.rel_text = rel_text
        self.rel_id = rel_id
