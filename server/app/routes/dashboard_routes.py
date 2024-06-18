from flask_restx import Namespace, Resource, fields
from app.services.dashboard_service import DashboardService, dashboard_ns, item_model, activity_model
from flask_jwt_extended import jwt_required, get_jwt_identity

@dashboard_ns.route('/inventory')
class InventoryOverview(Resource):
    @dashboard_ns.doc('get_inventory_overview')
    @dashboard_ns.marshal_list_with(item_model)
    def get(self):
        """Get basic inventory overview"""
        return DashboardService.get_inventory_overview(), 200


@dashboard_ns.route('/activities')
class RecentActivities(Resource):
    @dashboard_ns.doc('get_recent_activities')
    @dashboard_ns.marshal_list_with(activity_model)
    @jwt_required()
    def get(self):
        """Get recent activity log"""
        user_id = get_jwt_identity()
        return DashboardService.get_recent_activities(user_id), 200
