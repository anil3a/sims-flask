import os
from app import create_app, db
from flask.cli import FlaskGroup
from flask_migrate import Migrate
from flask_cors import CORS

config_name = os.getenv('FLASK_CONFIG', 'development')
app = create_app(config_name)
migrate = Migrate(app, db)

# Enable CORS for all routes
cors_allowed_origins = os.getenv('CORS_ALLOWED_ORIGINS', '*').split(',')
CORS(app, resources={r"/*": {"origins": cors_allowed_origins}})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
