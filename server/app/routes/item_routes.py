from flask import request
from flask_restx import Resource, Namespace, fields
from app.services.item_service import create_item, get_all_items, get_item, update_item, delete_item
from app.models import get_item_model

item_ns = Namespace('items', description='Item management operations')

# Register the item_model with the namespace
item_model = get_item_model(item_ns)

item_response_model = item_ns.model('ItemResponse', {
    'message': fields.String,
    'item': fields.Nested(item_model),
})

@item_ns.route('/')
class ItemList(Resource):
    @item_ns.doc('list_items')
    @item_ns.marshal_list_with(item_model)
    def get(self):
        """List all items"""
        return get_all_items()

    @item_ns.doc('create_item')
    @item_ns.expect(item_model)
    @item_ns.marshal_with(item_response_model, code=201)
    def post(self):
        """Create a new item"""
        data = request.get_json()
        return create_item(data)


@item_ns.route('/<int:item_id>')
@item_ns.response(404, 'Item not found')
@item_ns.param('item_id', 'The item identifier')
class Item(Resource):
    @item_ns.doc('get_item')
    @item_ns.marshal_with(item_model)
    def get(self, item_id):
        """Fetch a single item"""
        return get_item(item_id)

    @item_ns.doc('update_item')
    @item_ns.expect(item_model)
    @item_ns.marshal_with(item_model)
    def put(self, item_id):
        """Update an item"""
        data = request.get_json()
        return update_item(item_id, data)

    @item_ns.doc('delete_item')
    @item_ns.response(204, 'Item deleted')
    def delete(self, item_id):
        """Delete an item"""
        return delete_item(item_id)
