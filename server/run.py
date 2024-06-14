import os
from app import create_app, db
from flask.cli import FlaskGroup
from flask_migrate import Migrate

config_name = os.getenv('FLASK_CONFIG', 'development')
app = create_app(config_name)
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
