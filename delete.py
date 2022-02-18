from flask import Blueprint, request, redirect, abort
from db import review_db

delete = Blueprint(__name__, "delete")


@delete.route("/", methods=["POST"])
def delete_review_id():
    # Get review id from reviewlist.html
    review_id = int(request.form['review_id'])

    # Delete review
    record_exists = review_db.delete_review(review_id)

    if not record_exists:
        return abort(400, 'Record not found')

    # Redirect to list review
    return redirect('/list_reviews')
