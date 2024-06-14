from flask import request
from app.models import Item
from app import db
from flask_restx import Namespace

item_ns = Namespace('items', description='Item management operations')

def create_item(data):
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

def get_all_items():
    items = Item.query.all()
    return [{
        'id': item.id,
        'name': item.name,
        'quantity': item.quantity
    } for item in items], 200

def get_item(item_id):
    item = Item.query.get_or_404(item_id)
    return {
        'id': item.id,
        'name': item.name,
        'quantity': item.quantity
    }, 200

def update_item(item_id, data):
    item = Item.query.get_or_404(item_id)
    item.name = data.get('name')
    item.quantity = data.get('quantity')
    db.session.commit()

    return {"message": "Item updated successfully"}, 200

def delete_item(item_id):
    item = Item.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()

    return {"message": "Item deleted successfully"}, 200
