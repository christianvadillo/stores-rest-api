from app import app
from db import db

db.init_app(app)

""" Tells to SQLALchemy to create the tables defined in sqlite:///database.db
We no longer need create_table.py"""
@app.before_first_request  # execute this before first requeust
def create_tables():
    db.create_all()
