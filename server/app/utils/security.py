from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, decode_token, get_jwt_identity

bcrypt = Bcrypt()

def hash_password(password):
    """Hashes a password using bcrypt."""
    return bcrypt.generate_password_hash(password)

def check_password_hash(hashed_password, password):
    """Checks if a password matches its hashed version."""
    return bcrypt.check_password_hash(hashed_password, password)

def generate_access_token(identity):
    """Generates an access token for the given identity."""
    return create_access_token(identity=identity)

def decode_access_token(token):
    """Decodes an access token."""
    try:
        decoded_token = decode_token(token)
        return decoded_token
    except Exception as e:
        print(f"Error decoding token: {str(e)}")
        return None

def get_current_user():
    """Returns the current user's identity from the JWT."""
    return get_jwt_identity()
