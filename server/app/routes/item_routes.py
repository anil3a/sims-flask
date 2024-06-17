from app.services.item_service import ItemService, ItemServiceList, item_ns

item_ns.add_resource(ItemServiceList, '/')
item_ns.add_resource(ItemService, '/<int:item_id>')
