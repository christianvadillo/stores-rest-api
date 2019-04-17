from werkzeug.security import safe_str_cmp
from resources.user import UserModel

""" safe_str_cmp, safe string compare for any server"""


""" Authenticate an users"""


def authenticate(username, password):
    # getting username from database
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


""" takes an payload which contains de JWT Token and then
we will extract the user ID from that payload"""


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
