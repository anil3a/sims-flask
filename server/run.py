import os
from app import create_app, db
from flask import request, Response
from flask.cli import FlaskGroup
from flask_migrate import Migrate
from flask_cors import CORS

config_name = os.getenv('FLASK_CONFIG', 'development')
app = create_app(config_name)
migrate = Migrate(app, db)

# Enable CORS for all routes
cors_allowed_origins = os.getenv('CORS_ALLOWED_ORIGINS', '*').split(',')
CORS(app, resources={r"/*": {"origins": cors_allowed_origins}})

@app.before_request
def before_request():
    if request.method == 'OPTIONS':
        response = app.make_default_options_response()
        headers = response.headers

        origin = request.headers.get('Origin')
        if origin in cors_allowed_origins:
            headers['Access-Control-Allow-Origin'] = origin
            headers['Access-Control-Allow-Methods'] = 'POST, GET, OPTIONS, PUT, DELETE'
            headers['Access-Control-Allow-Headers'] = 'Authorization, Content-Type'

        return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
