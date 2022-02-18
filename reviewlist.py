from flask import Blueprint, render_template
from db import review_db

reviewlist = Blueprint(__name__, "reviewlist")


@reviewlist.route("/")
def list_of_reviews():
    all_reviews = review_db.get_reviews()
    return render_template("reviewlist.html", reviews=all_reviews)
