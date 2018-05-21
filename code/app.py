from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList
# flask restful removes need for jsonify method

app = Flask(__name__)
app.secret_key = 'secretstuff'
api = Api(app)

jwt = JWT(app, authenticate, identity) # Create endpoint /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=8001, debug=True)
