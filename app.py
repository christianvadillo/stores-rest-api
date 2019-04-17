import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT
from datetime import timedelta

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
""" When somebody makes a request to our API, that
request will be in the 'request' variable """

""" Resource is a thing that our API can return and
 create (usually mapped into database"""

""" JWT = JSON Web Token, essentially, we're going to be
encoding some data, used with users id"""

""" reqparse, can help us to only some elements can be pased through
the JSON payload """

# The app
app = Flask(__name__)

# Tell tu SQLALchemy where to find the database
# SQLALchemy database is gonna live at the root folder of our project
# and read database.db to work *It doesn't have to be SQLIte*
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///database.db')
# To replace the extension flask SQLALchemy that tracks changes we made
# For the main SQLALchemy library modification tracker which is better
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# key for encrypted data (should be secret)
app.secret_key = 'xxx'
# Allow us to add the resource to the app
api = Api(app)


"""JWT is going to use our app, the authenticate and identiy
functions (from security) together to allow for authentication of the users
and generate JWT token that can be send it to the next request we make, and
when it sent it, JWT calls the identity function and then it uses the JWT
token to get the user ID and with that it gets the correct user for that user
ID that JWT token represents"""

# Changing URI from /auth to /login
app.config['JWT_AUTH_URL_RULE'] = '/login'
# config JWT to expire within half an hour
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)

jwt = JWT(app, authenticate, identity)  # /auth


@jwt.auth_response_handler
def customized_response_handler(access_token, identity):
    return jsonify({
                    'access_token': access_token.decode('utf-8'),
                    'user_id': identity.id
    })


# Every resource has to be a class
# Class Item that inherits from Resource#


# Add the resource we created, so can be accessible via our api
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/Popo
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(StoreList, '/stores')


if __name__ == '__main__':
    """ We import Alchemy database here, because of
    a thing called circular imports """
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
