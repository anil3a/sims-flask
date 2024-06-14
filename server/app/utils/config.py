
def create_response(data, status_code=200):
    return data, status_code

def error_response(message, status_code=400):
    response = {
        'status': 'error',
        'message': message
    }
    return response, status_code

def validate_request_json(required_fields):
    def decorator(f):
        def wrapper(*args, **kwargs):
            request_json = request.get_json()
            for field in required_fields:
                if field not in request_json:
                    return error_response(f"'{field}' is required", 400)
            return f(*args, **kwargs)
        return wrapper
    return decorator
