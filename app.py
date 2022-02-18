from flask import Flask
from db import db

from index import index
from create import create
from reviewlist import reviewlist
from delete import delete
from aboutus import aboutus


app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///reviews.db'

# Blueprints for api
app.register_blueprint(index, url_prefix="/")
app.register_blueprint(create, url_prefix="/create_review")
app.register_blueprint(reviewlist, url_prefix="/list_reviews")
app.register_blueprint(delete, url_prefix="/delete_review")
app.register_blueprint(aboutus, url_prefix="/about_us")


def create_table():
    '''
    Create the tables in the database before first interaction
    '''
    with app.app_context():
        db.init_app(app)
        db.create_all()


if __name__ == '__main__':
    create_table()

    # Run web server
    app.run(debug=True, port=8080)
