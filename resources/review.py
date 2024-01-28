from flask_restful import Resource, fields, marshal_with, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import ReviewModel , db , UserModel

review_fields = {
    "id": fields.Integer,
    "comment": fields.String,
    "user_id": fields.Integer,
}

class ReviewResource(Resource):
    review_parser = reqparse.RequestParser()
    review_parser.add_argument('comment', type=str, help="Enter the comment")

    #getting the comments to dislay
    @marshal_with(review_fields)
    def get(self, review_id):
        review = ReviewModel.query.get(review_id)
        return review

     #user posting a comment
    @jwt_required
    @marshal_with(review_fields)
    def post(self):
        current_user_id = get_jwt_identity()
        data = ReviewResource.review_parser.parse_args()
 
        # Check if the user exists
        user = UserModel.query.get(current_user_id)
        if not user:
            return {"message": "User not found", "status": "fail"}, 404

        new_review = ReviewModel(
            comment=data['comment'],
            user_id=current_user_id
        )

        try:
            db.session.add(new_review)
            db.session.commit()
            return {"message": "Review created successfully", "status": "success"}, 201
        except:
            return {"message": "Unable to create review", "status": "fail"}, 500

    #user updating a comment
    @marshal_with(review_fields)
    def put(self, review_id):
        data = ReviewResource.review_parser.parse_args()

        # Fetch the review by ID
        review = ReviewModel.query.get(review_id)

        if not review:
            return {"message": "Review not found", "status": "fail"}, 404

        # Update the review
        review.comment = data['comment']

        try:
            db.session.commit()
            return {"message": "Review updated successfully", "status": "success"}, 200
        except:
            return {"message": "Unable to update review", "status": "fail"}, 500

    def delete(self, review_id):
        # Fetch the review by ID
        review = ReviewModel.query.get(review_id)

        if not review:
            return {"message": "Review not found", "status": "fail"}, 404

        try:
            db.session.delete(review)
            db.session.commit()
            return {"message": "Review deleted successfully", "status": "success"}, 200
        except:
            return {"message": "Unable to delete review", "status": "fail"}, 500
