""" internal representation of item.py
This code don't interact with direct the client, so
we can remove it from the item.py from resources package  """

from db import db

""" Sicen is an internal representation mode, it
has to contain the properties of an item as object
properties """


class StoreModel(db.Model):
    __tablename__ = 'stores'  # tablename where these model are going to stored
    # columns we want the table to contain
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    """" We've told SQLALchemy the 3 coluumns that This
    model is going to have (id,username, password must match
    the columns name)"""

    # Allows a store to see which items are in the item database
    # with store_id = own_store_id
    items = db.relationship('ItemModel', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    # return a JSON representation of the model
    def json(self):
        return {'name': self.name, 'items': list(map(lambda x: x.json(), self.items.all()))}

    @classmethod
    def find_by_name(cls, name):
        # connection = sqlite3.connect('database.db')
        # cursor = connection.cursor()
        #
        # # Retriving data from database
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query, (name,))
        # row = result.fetchone()  # The first result from the query
        # connection.close()
        #
        # if row:
        #     return cls(*row)  # return an ItemModel object instead of dictionary
        """Code above can be simplified using SQLALchemy"""
        """SELECT * FROM __tablename__ where name = name LIMIT 1 """
        return cls.query.filter_by(name=name).first()  # return an ItemModel Object

    def save_to_db(self):
        """Save and update the model to the database"""
        # connection = sqlite3.connect('database.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO items VALUES(?,?)"
        # cursor.execute(query, (self.name, self.price))
        #
        # connection.commit()
        # connection.close()
        """Code above can be simplified using SQLALchemy
        Same code insert and update a model in the database"""
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
