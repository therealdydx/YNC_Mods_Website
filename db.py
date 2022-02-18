from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Review(db.Model):
    '''
    The user responses will be made into an object called Review, and
    saved to the db (using model - carrying sets of properties that
    hold the data according to categories). Each data variable within the
    object is assigned a column within the db, and the data type etc.
    that it will take in.
    '''
    # Review id is the unique identifier, with autoincrement
    id = db.Column('review_id', db.Integer, primary_key=True)
    course_name = db.Column(db.String(100))
    course_code = db.Column(db.String(7))
    professor = db.Column(db.String(100))
    year = db.Column(db.Integer)
    rating = db.Column(db.Integer)
    workload = db.Column(db.Integer)
    grading = db.Column(db.Integer)
    review = db.Column(db.Text)

    '''
    __init__ is Constructor method. This function is used to
    take in the parameter, calls on itself, which allows assignment
    to the relevant class within the object.
    '''

    def __init__(self, course_name, course_code, professor,
                 year, rating, workload, grading, review):
        self.course_name = course_name
        self.course_code = course_code
        self.professor = professor
        self.year = year
        self.rating = rating
        self.workload = workload
        self.grading = grading
        self.review = review


class ReviewDatabase():
    '''
    This is a constructor that takes in the SQLAlchemy db object.
    '''

    def __init__(self, db):
        self.db = db

    def insert_review(self, course_name, course_code, professor, year, rating,
                      workload, grading, review):
        '''
        This function is used to insert a review into the database.
        '''
        # Add review to the database by making it an object and adding to db
        review_object = Review(course_name, course_code, professor, year,
                               rating, workload, grading, review)
        self.db.session.add(review_object)
        self.db.session.commit()

    def delete_review(self, review_id):
        '''
        Deletes a review from the database
        '''

        exists = Review.query.filter_by(id=review_id).first() is not None
        if exists:
            Review.query.filter_by(id=review_id).delete()
            self.db.session.commit()

        return exists

    def get_reviews(self):
        '''
        This function is used to get all the reviews from the database
        '''
        return Review.query.all()


review_db = ReviewDatabase(db)
