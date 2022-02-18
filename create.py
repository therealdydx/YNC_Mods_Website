from flask import Blueprint, request, render_template, redirect, abort
from datetime import date
from db import review_db

create = Blueprint(__name__, "create")


@create.route("/", methods=["GET"])
def show_create_form():
    '''
    This function sets a limit for the max year to be the current year,
    to minimise inaccurate answers i.e. years that has not happened. This is
    integrated with the html form entry.
    '''
    return render_template("createreview.html", max_year=date.today().year)


@create.route("/", methods=['POST'])
def create_review():
    '''
    This function gets the information inputted by the user from the
    html form fields and saves them to respective variables,
    allowing the user to create a review front-end, which writes onto
    the db back-end.
    '''

    try:
        # user response are saved to respective variables
        course_name = request.form["course_name"]
        course_code = request.form["course_code"]
        professor = request.form["professor"]
        year = int(request.form["year"])
        rating = int(request.form["rating"])
        workload = int(request.form["workload"])
        grading = int(request.form["grading"])
        review = request.form["review"]

        # Insert review into the database
        review_db.insert_review(course_name, course_code, professor,
                                year, rating, workload, grading, review)

        # Redirect to list of reviews once the user's review has been
        # written to db
        return redirect('/list_reviews')
    except ValueError:
        return abort(400, 'Invalid input')
