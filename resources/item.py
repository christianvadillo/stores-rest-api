from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):
    """Defining the parser to avoid 'name' changes, just 'price'
        be allowed to change his info"""
    parser = reqparse.RequestParser()
    parser.add_argument('price',
                        type=float,  # Type of variable
                        required=True,  # make sure that no request can come through with no price
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('store_id',
                        type=int,  # Type of variable
                        required=True,  # make sure that no request can come through with no price
                        help="Every item needs a store id"
                        )
    # decorator that forces us to authenticate before we
    # can call the get method
    @jwt_required()
    # Return item
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()  # sinces ItemModel now return objects, we need to use .json() to parse it
        return {'message': 'Item not found'}, 404

    # Create item
    def post(self, name):
        """ if we found an item matching this name and it is not None,
        return a message that the item already exists"""
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' alread exists.".format(name)}, 400

        data = Item.parser.parse_args()
        # item = {'name': name, 'price': data['price']}
        item = ItemModel(name, **data)  # now it will return an ItemModel object

        try:
            item.save_to_db()
        except Exception:
            return {'message': "An error occurred inserting the item."}, 500  # Internal Server error

        return item.json(), 201  # for that the application knows tha this has happened (201 = Created)

    # Delete item
    def delete(self, name):
        # assigning the elment that we want to delete
        item = ItemModel.find_by_name(name)
        if item:
            # connection = sqlite3.connect('database.db')
            # cursor = connection.cursor()
            # query = "DELETE FROM items WHERE name = ?"
            #
            # cursor.execute(query, (name,))
            # connection.commit()
            # connection.close()
            # return {'message': 'Item deleted'}, 200
            item.delete_from_db()
            return {'message': 'Item deleted'}
        return {'message': 'Item not found'}, 400

    # Create or update an items
    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            # If don't find anything, create a new one
            # item = ItemModel(name, data['price'], data['store_id'])
            item = ItemModel(name, **data)
        else:
            # If it exists, update the price column
            item.price = data['price']

        item.save_to_db()  # SQLALchemy will save the changes
        return item.json()


class ItemList(Resource):
    def get(self):
        # connection = sqlite3.connect('database.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM items"
        # results = cursor.execute(query)
        # items = []
        #
        # for row in results:
        #     items.append({'name': row[0], 'price': row[1]})
        #
        # cursor.close()

        # return {'items': list(map(lambda x: x.json, ItemModel.query.all()))} #using lambda
        return {'items': [item.json() for item in ItemModel.query.all()]}
