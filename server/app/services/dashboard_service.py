from flask import request
from app import db
from flask_restx import Resource, Namespace, fields
from app.models import Item, ActivityLog, User
from app.api_models import get_item_model, get_dashboard_activity_model

dashboard_ns = Namespace('dashboard', description='Dashboard operations')
item_model = get_item_model(dashboard_ns)
activity_model = get_dashboard_activity_model(dashboard_ns)


class DashboardService:
    @staticmethod
    def get_inventory_overview():
        """
        Retrieve an overview of all inventory items.

        Returns:
            list: A list of dictionaries containing item details (id, name, quantity).
        """
        return Item.query.all()

    @staticmethod
    def get_recent_activities(user_id):
        """
        Retrieve a log of recent activities.

        Returns:
            list: A list of dictionaries containing activity details (id, action, timestamp, user's full name).
        """
        user = User.query.filter_by(username=user_id).first()
        if not user:
            raise ValueError('User not found')
        activities = ActivityLog.query.filter(ActivityLog.user_id==user.id).order_by(ActivityLog.timestamp.desc()).limit(10).all()

        activity_log = [{
            "id": activity.id,
            "action": activity.action,
            "timestamp": activity.timestamp,
            "name": f"{activity.user.firstname} {activity.user.lastname}"
        } for activity in activities]
        return activity_log
