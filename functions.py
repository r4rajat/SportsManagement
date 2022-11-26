import constant
from config import mongo


def login(username, password):
    db = mongo['sports-management']
    coll = db['users']
    try:
        data = coll.find_one({
            constant.USER_NAME: username
        })
    except Exception as e:
        return Exception(e)

    if data is not None:
        if password == data[constant.PASSWORD]:
            return True
        else:
            return False
    else:
        return False


def register(full_name, username, password, email, gender, age, sport):
    db = mongo['sports-management']
    coll = db['users']
    try:
        try:
            data = coll.find_one({
                constant.USER_NAME: username
            })
        except Exception as e:
            return Exception(e)
        if data is not None:
            return "User with Username " + username + " Already Exists"

        data = coll.insert_one({
            constant.USER_NAME: username,
            constant.PASSWORD: password,
            constant.FULL_NAME: full_name,
            constant.EMAIL: email,
            constant.GENDER: gender,
            constant.AGE: age,
            constant.SPORT: sport
        })
    except Exception as e:
        return Exception(e)

    if data:
        return True
    else:
        return False