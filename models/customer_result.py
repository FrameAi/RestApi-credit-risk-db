from db import db
from datetime import datetime

# Tell SQLAlchemy this is an object we want to map(ORM) by inheriting db.Model

class CustomerResultModel(db.Model):
    # tell SQLAlchemy table name
    __tablename__ = 'customer_results'

    id = db.Column(db.Integer(), primary_key=True, autoincrement = True)
    probability_of_default_next_month = db.Column(db.Numeric(precision=2, scale=2, asdecimal=False, decimal_return_scale=None))
    feedback_did_default = db.Column(db.Boolean(), nullable=True)
    
    # One to One bidirectional (one customer_result to one customer)
    # cascading: delete customers if delete customerresult (cascade on delete) (default value of cascade is save-update, merge)
    customer = db.relationship('CustomerModel', back_populates='customer_result', lazy='dynamic', cascade='delete, save-update, merge')

    last_updated = db.Column(db.TIMESTAMP(timezone=False))
   

    def __init__(self, probability_of_default_next_month, feedback_did_default):
        self.probability_of_default_next_month = probability_of_default_next_month
        self.feedback_did_default = feedback_did_default
        self.last_updated = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') # generate createdAt date on our server

    def update_customer_result(self, probability_of_default_next_month, feedback_did_default):
        self.probability_of_default_next_month = probability_of_default_next_month
        self.feedback_did_default = feedback_did_default
        self.last_updated = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') # generate createdAt date on our server

    # calling json() method is slow when calling self.chat_posts.all() due to lazy='dynamic' relationship
    def json(self):
        return {'id': self.id, 'probability_of_default_next_month': self.probability_of_default_next_month, 'feedback_did_default': self.feedback_did_default, 'last_updated': self.last_updated.strftime('%Y-%m-%d %H:%M:%S')}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
