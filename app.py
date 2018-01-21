import os # to import credentials from env variables on the machine
import mysql.connector # driver for MySQL
#import mysql.connector
from flask import Flask
from flask_restful import Api

# JWT, rate limiting by remote address
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

#import resources
from resources.user import UserRegister, UserProfile, UserProfileList, UserLogin
from resources.customer import Customer, CustomerList
from resources.customer_result import CustomerResult, CustomerResultList


app = Flask(__name__)
api = Api(app) # used to add resources and configure our api

# get env variable for db credentials, if not found, use our sqlite for testing in our local env
# (we can use sqlite on the server, however Heroku dyno's free plan get reset and wiped periodically)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

# Flask-SQLAlchemy has its own event notification system that gets layered on top of SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Setup the Flask-JWT-Extended extension (The secret key is needed to keep the client-side sessions secure)
app.secret_key = os.environ.get('CONSUMER_RISK_SECRET_KEY')
jwt = JWTManager(app)


# SqlAlchemy can create db for us
# Use flask decorator 
# before first request run: app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db' unless it already exists
@app.before_first_request
def create_tables():
    db.create_all() # only creates tables that it sees



# START add resources

# allow users to register and obtain JWT tokens
api.add_resource(UserRegister, '/register')
# allow users to login and obtain JWT tokens
api.add_resource(UserLogin, '/login')
# perform CRUD operations on users
api.add_resource(UserProfile, '/user-profile/<string:email>')
# list all user profiles
api.add_resource(UserProfileList, '/user-profiles')


# perform CRUD operations on customers
api.add_resource(Customer, '/customer/<string:related_user_id>')
# list all customers
api.add_resource(CustomerList, '/customers')


# perform CRUD operations on CustomerResults
api.add_resource(CustomerResult, '/customer-result/<string:theId>')
# list all CustomerResults
api.add_resource(CustomerResultList, '/customer-result')

# END add resources



# __name__ is a built-in variable which evaluates to the name of the current module. 
# if a module is being run directly (e.g python myscript.py above), then __name__ is set to the string "__main__". and the code in the if statement will run
if __name__ == '__main__':
	# avoid Circular imports
	# Our item and models, import db as well.
	# If we import db at top, and import models at top, we have a circular import
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True) # TODO: REMOVE DEBUG IN PRODUCTION
    # PORT 5432
