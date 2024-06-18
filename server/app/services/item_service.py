from flask import request
from app import db
from flask_restx import Resource, Namespace, fields
from app.models import Item, ActivityLog
from app.api_models import get_item_model, get_new_item_model, get_response_item_model, log_activity
from flask_jwt_extended import jwt_required, get_jwt_identity

item_ns = Namespace('items', description='Item management operations')
item_model = get_item_model(item_ns)
item_new_model = get_new_item_model(item_ns)
item_response_model = get_response_item_model(item_ns)

@item_ns.route('/')
class ItemServiceList(Resource):
    @item_ns.doc('list_items', params={
        'name': 'Filter by item name',
        'min_quantity': 'Minimum quantity filter',
        'max_quantity': 'Maximum quantity filter'
    })
    @item_ns.marshal_list_with(item_model)
    @jwt_required()
    def get(self):
        """List all items"""
        query_params = request.args
        name_filter = query_params.get('name')
        min_quantity = query_params.get('min_quantity')
        max_quantity = query_params.get('max_quantity')

        items_query = Item.query

        if name_filter:
            items_query = items_query.filter(Item.name.ilike(f'%{name_filter}%'))
        if min_quantity:
            items_query = items_query.filter(Item.quantity >= int(min_quantity))
        if max_quantity:
            items_query = items_query.filter(Item.quantity <= int(max_quantity))

        items = items_query.all()
        return items, 200

    @item_ns.doc('create_item')
    @item_ns.expect(item_new_model)
    @item_ns.marshal_with(item_response_model, code=201)
    @jwt_required()
    def post(self):
        """Create a new item"""
        user_id = get_jwt_identity()

        data = request.get_json()
        name = data.get('name')
        quantity = data.get('quantity')

        new_item = Item(name=name, quantity=quantity)
        db.session.add(new_item)
        db.session.commit()

        log_activity(
            user_id,
            f"Created item [{new_item.id}]: {new_item.name} (quantity: {new_item.quantity})",
            rel_text="item",
            rel_id=new_item.id
        )

        return {
            "message": "Item created successfully",
            "item": new_item
        }, 201


@item_ns.route('/<int:item_id>')
@item_ns.response(404, 'Item not found')
@item_ns.param('item_id', 'The item identifier')
class ItemService(Resource):
    @item_ns.doc('get_item')
    @item_ns.marshal_with(item_model)
    @jwt_required()
    def get(self, item_id):
        """Fetch a single item"""
        item = Item.query.get_or_404(item_id)
        return item, 200

    @item_ns.doc('update_item')
    @item_ns.expect(item_new_model)
    @item_ns.marshal_with(item_response_model)
    @jwt_required()
    def put(self, item_id):
        """Update an item"""
        user_id = get_jwt_identity()
        data = request.get_json()

        item = Item.query.get_or_404(item_id)
        item.name = data.get('name')
        item.quantity = data.get('quantity')
        db.session.commit()

        log_activity(
            user_id,
            f"Updated item [{item.id}]: {item.name} (quantity: {item.quantity})",
            rel_text="item",
            rel_id=item.id
        )

        return {
            "message": "Item updated successfully",
            "item": item
        }, 200

    @item_ns.doc('delete_item')
    @item_ns.response(204, 'Item deleted')
    @jwt_required()
    def delete(self, item_id):
        """Delete an item"""
        user_id = get_jwt_identity()
        item = Item.query.get_or_404(item_id)

        db.session.delete(item)
        db.session.commit()

        log_activity(
            user_id,
            f"Deleted item [{item.id}]: {item.name} (quantity: {item.quantity})",
            rel_text="item",
            rel_id=item.id
        )

        return {"message": "Item deleted successfully"}, 200
