from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, jwt_refresh_token_required
from models.customer_result import CustomerResultModel

class CustomerResult(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('probability_of_default_next_month',
        type=float,
        required=True,
        help="probability_of_default_next_month field cannot be blank."
    )
    parser.add_argument('feedback_did_default',
        type=bool,
        required=True,
        help="feedback_did_default field cannot be blank."
    )

    @jwt_refresh_token_required
    def get(self, theId):

        theCustomerResult = CustomerResultModel.find_by_id(theId)
        if theCustomerResult:
            return theCustomerResult.json()
        return {'message': 'customer_result with id \'' + theId + '\' not found'}, 404

    @jwt_refresh_token_required
    def post(self, theId):

        data = CustomerResult.parser.parse_args()
        theCustomerResult = CustomerResultModel(data['probability_of_default_next_month'], data['feedback_did_default'])

        try:
            theCustomerResult.save_to_db()
        except:
            return {"message": "An error occurred inserting the item."}, 500

        return theCustomerResult.json(), 201

    @jwt_refresh_token_required
    def put(self, theId):

        data = CustomerResult.parser.parse_args()
        theCustomerResult = CustomerResultModel.find_by_id(theId)

        if theCustomerResult:
            # update if exists
            theCustomerResult.update_customer_result(data['probability_of_default_next_month'], data['feedback_did_default'])
        else:
            # create if dne
            theCustomerResult = CustomerResultModel(data['probability_of_default_next_month'], data['feedback_did_default'])
        
        theCustomerResult.save_to_db()

        return theCustomerResult.json()

    @jwt_required
    def delete(self, theId):

        theCustomerResult = CustomerResultModel.find_by_id(theId)

        if theCustomerResult:
            theCustomerResult.delete_from_db()

        return {'message': 'CustomerResult deleted'}


class CustomerResultList(Resource):
    # list all chat posts
    @jwt_required
    def get(self):
        # apply   lambda x: x.json() to each element in the list
        return {'CustomerResults': list(map(lambda x: x.json(), CustomerResultModel.query.all()))}

        # list comprehension
        # return {'items': [item.json() for item in ItemModel.query.all()]}



