from app.services.auth_service import RegisterService, LoginService, auth_ns

auth_ns.add_resource(RegisterService, '/register')
auth_ns.add_resource(LoginService, '/login')
