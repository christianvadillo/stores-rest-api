# Retrieve users objects from database
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'  # tablename where these model are going to stored
    # columns we want the table to contain
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(10))
    """" We've told SQLALchemy the 3 coluumns that This
    model is going to have (id,username, password must match
    the columns name)"""

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

# find username in databse by id
    @classmethod  # becausue we are passing 'self' but not using it, we change self for cls
    def find_by_username(cls, username):
        # connection = sqlite3.connect('database.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE username = ?"
        # result = cursor.execute(query, (username,))  # Paramemters always have to be in the form of a tuple (par1,) or (par1,par2,)
        # row = result.fetchone()  # get the first row of result
        # if row:
        #     user = cls(*row)  # Create an instance of User with the data retrieved from database. Using *row instead of row[0],row[1],row[2]
        # else:
        #     user = None
        #
        # connection.close()
        return cls.query.filter_by(username=username).first()

# find username in databse by id
    @classmethod  # becausue we are passing 'self' but not using it, we change self for cls
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('database.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE id = ?"
        # result = cursor.execute(query, (_id,))  # Paramemters always have to be in the form of a tuple (par1,) or (par1,par2,)
        # row = result.fetchone()  # get the first row of result
        # if row:
        #     user = cls(*row)  # Create an instance of User with the data retrieved from database. Using *row instead of row[0],row[1],row[2]
        # else:
        #     user = None
        #
        # connection.close()
        return cls.query.filter_by(id=_id).first()
