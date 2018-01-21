from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
from models.customer import CustomerModel

from models.customer import EducationType
from models.customer import MaritalStatusType

class Customer(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('credit_limit_balance',
        type=int,
        required=True,
        help="credit_limit_balance field cannot be left blank"
    )
    parser.add_argument('education',
        type=int,
        choices=(1,2,3,4),
        required=True,
        help="education field cannot be left blank, and must be a valid choice"
    )
    parser.add_argument('marriage',
        type=int,
        choices=(1,2,3),
        required=True,
        help="marriage field cannot be left blank"
    )
    parser.add_argument('age',
        type=int,
        required=True,
        help="age field cannot be left blank"
    )

    parser.add_argument('repayment_status_month_1',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('repayment_status_month_2',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('repayment_status_month_3',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('repayment_status_month_4',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('repayment_status_month_5',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('repayment_status_month_6',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )

    parser.add_argument('bill_amount_month_1',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('bill_amount_month_2',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('bill_amount_month_3',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('bill_amount_month_4',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('bill_amount_month_5',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('bill_amount_month_6',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )

    parser.add_argument('payment_amount_month_1',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('payment_amount_month_2',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('payment_amount_month_3',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('payment_amount_month_4',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('payment_amount_month_5',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )
    parser.add_argument('payment_amount_month_6',
        type=int,
        required=True,
        help="This field cannot be left blank"
    )

    parser.add_argument('customer_result_id',
        type=int,
        required=True,
        help="customer_result_id field cannot be left blank"
    )


    @jwt_refresh_token_required
    def get(self, related_user_id):

        theCustomer = CustomerModel.find_recent_by_related_user_id(related_user_id)
        if theCustomer:
            return theCustomer.json()
        return {'message': 'customer with related_user_id \'' + related_user_id + '\' not found'}, 404

    @jwt_refresh_token_required
    def post(self, related_user_id):

        data = Customer.parser.parse_args()

        theCustomer = CustomerModel(data['credit_limit_balance'], EducationType(data['education']), MaritalStatusType(data['marriage']), data['age'], data['repayment_status_month_1'], 
            data['repayment_status_month_2'], data['repayment_status_month_3'], data['repayment_status_month_4'], data['repayment_status_month_5'], 
            data['repayment_status_month_6'], data['bill_amount_month_1'], data['bill_amount_month_2'], data['bill_amount_month_3'], data['bill_amount_month_4'], 
            data['bill_amount_month_5'], data['bill_amount_month_6'], data['payment_amount_month_1'], data['payment_amount_month_2'], data['payment_amount_month_3'], 
            data['payment_amount_month_4'], data['payment_amount_month_5'], data['payment_amount_month_6'], related_user_id, data['customer_result_id'])
        
        # OR USE: theCustomer = CustomerModel(related_user_id, **data) # **kwargs is a dictionary (key word args)

        try:
            theCustomer.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500

        return theCustomer.json(), 201

    # NOT NEEDED
    @jwt_required
    def put(self, related_user_id):

        data = Customer.parser.parse_args()
        theCustomer = CustomerModel.find_recent_by_related_user_id(related_user_id)

        if theCustomer:
            # update if exists
            theCustomer.update_customer(data['credit_limit_balance'], EducationType(data['education']), MaritalStatusType(data['marriage']), data['age'], data['repayment_status_month_1'], 
                data['repayment_status_month_2'], data['repayment_status_month_3'], data['repayment_status_month_4'], data['repayment_status_month_5'], 
                data['repayment_status_month_6'], data['bill_amount_month_1'], data['bill_amount_month_2'], data['bill_amount_month_3'], data['bill_amount_month_4'], 
                data['bill_amount_month_5'], data['bill_amount_month_6'], data['payment_amount_month_1'], data['payment_amount_month_2'], data['payment_amount_month_3'], 
                data['payment_amount_month_4'], data['payment_amount_month_5'], data['payment_amount_month_6'], related_user_id, data['customer_result_id'])
        else:
            # create if dne
            theCustomer = CustomerModel(data['credit_limit_balance'], EducationType(data['education']), MaritalStatusType(data['marriage']), data['age'], data['repayment_status_month_1'], 
                data['repayment_status_month_2'], data['repayment_status_month_3'], data['repayment_status_month_4'], data['repayment_status_month_5'], 
                data['repayment_status_month_6'], data['bill_amount_month_1'], data['bill_amount_month_2'], data['bill_amount_month_3'], data['bill_amount_month_4'], 
                data['bill_amount_month_5'], data['bill_amount_month_6'], data['payment_amount_month_1'], data['payment_amount_month_2'], data['payment_amount_month_3'], 
                data['payment_amount_month_4'], data['payment_amount_month_5'], data['payment_amount_month_6'], related_user_id, data['customer_result_id'])
        
            # OR USE: theCustomer = CustomerModel(related_user_id, **data)
        
        theCustomer.save_to_db()

        return theCustomer.json()

    @jwt_required
    def delete(self, related_user_id):

        theCustomer = CustomerModel.find_recent_by_related_user_id(related_user_id)

        if theCustomer:
            theCustomer.delete_from_db()

        return {'message': 'theCustomer deleted'}


class CustomerList(Resource):
    # list all chat posts
    @jwt_required
    def get(self):
        # apply   lambda x: x.json()   to each element in the list
        return {'Customers': list(map(lambda x: x.json(), CustomerModel.query.all()))}

        # list comprehension
        # return {'items': [item.json() for item in ItemModel.query.all()]}


