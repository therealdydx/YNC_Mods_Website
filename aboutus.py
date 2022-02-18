from flask import Blueprint, render_template

aboutus = Blueprint(__name__, "aboutus")


@aboutus.route("/")
def about_us():
    return render_template("aboutus.html")
