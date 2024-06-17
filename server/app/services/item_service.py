from flask import request
from app.models import Item
from app import db
from flask_restx import Resource, Namespace, fields
from app.models import get_item_model

item_ns = Namespace('items', description='Item management operations')

# Register the item_model with the namespace
item_model = get_item_model(item_ns)

item_response_model = item_ns.model('ItemResponse', {
    'message': fields.String,
    'item': fields.Nested(item_model),
})

@item_ns.route('/')
class ItemServiceList(Resource):
    @item_ns.doc('list_items', params={
        'name': 'Filter items by name',
        'min_quantity': 'Minimum quantity filter',
        'max_quantity': 'Maximum quantity filter'
    })
    @item_ns.marshal_list_with(item_model)
    def get(self):
        """
        List all items

        Supports parameters searching and filtering result
        """
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
        return [{
            'id': item.id,
            'name': item.name,
            'quantity': item.quantity
        } for item in items], 200

    @item_ns.doc('create_item')
    @item_ns.expect(item_model)
    @item_ns.marshal_with(item_response_model, code=201)
    def post(self):
        """Create a new item"""
        data = request.get_json()
        name = data.get('name')
        quantity = data.get('quantity')
        new_item = Item(name=name, quantity=quantity)
        db.session.add(new_item)
        db.session.commit()
        return {
            "message": "Item created successfully",
            "item": {
                "id": new_item.id,
                "name": new_item.name,
                "quantity": new_item.quantity
            }
        }, 201


@item_ns.route('/<int:item_id>')
@item_ns.response(404, 'Item not found')
@item_ns.param('item_id', 'The item identifier')
class ItemService(Resource):
    @item_ns.doc('get_item')
    @item_ns.marshal_with(item_model)
    def get(self, item_id):
        """Fetch a single item"""
        item = Item.query.get_or_404(item_id)
        return {
            'id': item.id,
            'name': item.name,
            'quantity': item.quantity
        }, 200

    @item_ns.doc('update_item')
    @item_ns.expect(item_model)
    @item_ns.marshal_with(item_model)
    def put(self, item_id):
        """Update an item"""
        data = request.get_json()
        item = Item.query.get_or_404(item_id)
        item.name = data.get('name')
        item.quantity = data.get('quantity')
        db.session.commit()
        return {"message": "Item updated successfully"}, 200

    @item_ns.doc('delete_item')
    @item_ns.response(204, 'Item deleted')
    def delete(self, item_id):
        """Delete an item"""
        item = Item.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message": "Item deleted successfully"}, 200
