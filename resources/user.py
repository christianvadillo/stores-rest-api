from flask_restful import Resource, reqparse
from models.user import UserModel
# Resource added to the API for user register


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        # find if the user exists
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        # connection = sqlite3.connect('database.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO users VALUES (NULL, ?, ?)"  # NULL for id, because we have an auto increment column
        # cursor.execute(query, (data['username'], data['password']))
        #
        # connection.commit()
        # connection.close()
        # user = UserModel(data['username'], data['password'])
        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201
