from flask import Blueprint, render_template

index = Blueprint(__name__, "index")


@index.route("/")
def home_page():
    return render_template("index.html")
