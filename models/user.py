from db import db
from datetime import datetime

# Tell SQLAlchemy this is an object we want to map(ORM) by inheriting db.Model

class UserModel(db.Model):
    # tell SQLAlchemy table name
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True, autoincrement = True)
    email = db.Column(db.String(200))
    password = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP(timezone=False))

    # One to Many bidirectional (one user has many customers)
    '''
    (establishment of an event listener on both sides which will mirror attribute operations in both directions
    “when an append or set event occurs here, set ourselves onto the incoming attribute using this particular attribute name”.)
    
    dynamic: enable management of a large collection using a dynamic relationship. 
    returns a Query object in place of a collection.  filter() criterion may be applied as well as limits and offsets
    ex: do not go into customers table and do not load each object for each table unless we specify (use self.customers.all() instead of self.customers)
    '''
     # cascading: delete customers if delete user (cascade on delete) (default value of cascade is save-update, merge)
    customers = db.relationship('CustomerModel', back_populates='user', lazy='dynamic', cascade='delete, save-update, merge')
   

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') # generate createdAt date on our server

    # calling json() method is slow when calling self.chat_posts.all() due to lazy='dynamic' relationship
    def json(self):
        return {'id': self.id, 'email': self.email, 'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'), 'customers': [customers.json() for customers in self.customers.all()]}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        # get first row (sqlAlchemy then converts it to user model object)
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
