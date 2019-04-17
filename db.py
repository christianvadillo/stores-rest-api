from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

""" SQLAlchemy essentially is going to link to
our flask app and it's going to look at all of the
objects that we tell it to, then it will allow us to
map those objects to rows in a database"""
