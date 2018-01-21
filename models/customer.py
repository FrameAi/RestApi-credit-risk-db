from db import db
from datetime import datetime
import enum


class EducationType(enum.Enum):
    graduate_school = 1
    university = 2
    high_school = 3
    others = 4

class MaritalStatusType(enum.Enum):
    married = 1
    single = 2
    other = 3



class CustomerModel(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    credit_limit_balance = db.Column(db.Integer)
    education = db.Column(db.Enum(EducationType))
    marriage = db.Column(db.Enum(MaritalStatusType))
    age = db.Column(db.SmallInteger)

    repayment_status_month_1 = db.Column(db.SmallInteger)
    repayment_status_month_2 = db.Column(db.SmallInteger)
    repayment_status_month_3 = db.Column(db.SmallInteger)
    repayment_status_month_4 = db.Column(db.SmallInteger)
    repayment_status_month_5 = db.Column(db.SmallInteger)
    repayment_status_month_6 = db.Column(db.SmallInteger)

    bill_amount_month_1 = db.Column(db.Integer)
    bill_amount_month_2 = db.Column(db.Integer)
    bill_amount_month_3 = db.Column(db.Integer)
    bill_amount_month_4 = db.Column(db.Integer)
    bill_amount_month_5 = db.Column(db.Integer)
    bill_amount_month_6 = db.Column(db.Integer)

    payment_amount_month_1 = db.Column(db.Integer)
    payment_amount_month_2 = db.Column(db.Integer)
    payment_amount_month_3 = db.Column(db.Integer)
    payment_amount_month_4 = db.Column(db.Integer)
    payment_amount_month_5 = db.Column(db.Integer)
    payment_amount_month_6 = db.Column(db.Integer)

    # which user does this customer belong to (which user looked up this customer)
    related_user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    # Many to One bidirectional (many customers to one user)
    # cascading: do not delete user if delete customer (do not cascade on delete (default value of cascade is save-update, merge)
    user = db.relationship('UserModel', back_populates='customers', cascade='save-update, merge')
    

    # this customer has a customer result
    customer_result_id = db.Column(db.Integer, db.ForeignKey('customer_results.id'))
    # One to One bidirectional (one customer to one customer result) 
    # (uselist:  one to many forms a list, many to one forms a scalar, many to many is a list. we need a scalar since we have a bi-directional one-to-one relationship, set uselist to False)
    # cascading: delete customer_result if delete customer (default value of cascade is save-update, merge)
    customer_result = db.relationship("CustomerResultModel", uselist=False, back_populates="customer", cascade='delete, save-update, merge')

    created_at = db.Column(db.TIMESTAMP(timezone=False))

    # =========================================

    def __init__(self, credit_limit_balance, education, marriage, age, repayment_status_month_1, repayment_status_month_2, 
                repayment_status_month_3, repayment_status_month_4, repayment_status_month_5, repayment_status_month_6, 
                bill_amount_month_1, bill_amount_month_2, bill_amount_month_3, bill_amount_month_4, bill_amount_month_5, bill_amount_month_6,
                payment_amount_month_1, payment_amount_month_2, payment_amount_month_3, payment_amount_month_4, payment_amount_month_5, payment_amount_month_6,
                related_user_id, customer_result_id):

        self.credit_limit_balance = credit_limit_balance
        self.education = education
        self.marriage = marriage
        self.age = age

        self.repayment_status_month_1 = repayment_status_month_1
        self.repayment_status_month_2 = repayment_status_month_2
        self.repayment_status_month_3 = repayment_status_month_3
        self.repayment_status_month_4 = repayment_status_month_4
        self.repayment_status_month_5 = repayment_status_month_5
        self.repayment_status_month_6 = repayment_status_month_6

        self.bill_amount_month_1 = bill_amount_month_1
        self.bill_amount_month_2 = bill_amount_month_2
        self.bill_amount_month_3 = bill_amount_month_3
        self.bill_amount_month_4 = bill_amount_month_4
        self.bill_amount_month_5 = bill_amount_month_5
        self.bill_amount_month_6 = bill_amount_month_6

        self.payment_amount_month_1 = payment_amount_month_1
        self.payment_amount_month_2 = payment_amount_month_2
        self.payment_amount_month_3 = payment_amount_month_3
        self.payment_amount_month_4 = payment_amount_month_4
        self.payment_amount_month_5 = payment_amount_month_5
        self.payment_amount_month_6 = payment_amount_month_6

        self.related_user_id = related_user_id
        self.customer_result_id = customer_result_id

        self.created_at = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S') # generate createdAt date on our server


    @classmethod
    def find_recent_by_related_user_id(cls, to_find_related_user_id):
        return cls.query.filter_by(related_user_id=to_find_related_user_id).order_by('created_at desc').first()


    def json(self):
        return {'id': self.id, 'credit_limit_balance': self.credit_limit_balance, 'education': str(self.education).split('.')[1], 'marriage': str(self.marriage).split('.')[1], 'created_at': self.created_at.strftime('%c'), 'related_user_id': self.related_user_id}

    # for update AND insert
    def save_to_db(self):
        # aession a collection of ojects we will write to the db
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    def update_customer(self, credit_limit_balance, education, marriage, age, repayment_status_month_1, repayment_status_month_2, 
    	repayment_status_month_3, repayment_status_month_4, repayment_status_month_5, repayment_status_month_6, 
    	bill_amount_month_1, bill_amount_month_2, bill_amount_month_3, bill_amount_month_4, bill_amount_month_5, bill_amount_month_6,
    	payment_amount_month_1, payment_amount_month_2, payment_amount_month_3, payment_amount_month_4, payment_amount_month_5, payment_amount_month_6,
    	related_user_id, customer_result_id):

        self.credit_limit_balance = credit_limit_balance
        self.education = education
        self.marriage = marriage
        self.age = age

        self.repayment_status_month_1 = repayment_status_month_1
        self.repayment_status_month_2 = repayment_status_month_2
        self.repayment_status_month_3 = repayment_status_month_3
        self.repayment_status_month_4 = repayment_status_month_4
        self.repayment_status_month_5 = repayment_status_month_5
        self.repayment_status_month_6 = repayment_status_month_6

        self.bill_amount_month_1 = bill_amount_month_1
        self.bill_amount_month_2 = bill_amount_month_2
        self.bill_amount_month_3 = bill_amount_month_3
        self.bill_amount_month_4 = bill_amount_month_4
        self.bill_amount_month_5 = bill_amount_month_5
        self.bill_amount_month_6 = bill_amount_month_6

        self.payment_amount_month_1 = payment_amount_month_1
        self.payment_amount_month_2 = payment_amount_month_2
        self.payment_amount_month_3 = payment_amount_month_3
        self.payment_amount_month_4 = payment_amount_month_4
        self.payment_amount_month_5 = payment_amount_month_5
        self.payment_amount_month_6 = payment_amount_month_6

        self.related_user_id = related_user_id
        self.customer_result_id = customer_result_id

