from .auth_routes import auth_ns
from .item_routes import item_ns
from .dashboard_routes import dashboard_ns

def register_blueprints(app, api):
    api.add_namespace(auth_ns, path='/auth')
    api.add_namespace(item_ns, path='/items')
    api.add_namespace(dashboard_ns, path='/dashboard')
