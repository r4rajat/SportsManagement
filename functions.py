import constant
from config import mongo


def login(username, password):
    db = mongo['sports-management']
    coll = db['users']
    data = coll.find_one({
        constant.USER_NAME: username
    })
    if len(data) != 0:
        if password == data[constant.PASSWORD]:
            return True
        else:
            return False
    else:
        return False


def register(username, password, email, gender, age, sport):
    db = mongo['sports-management']
    coll = db['users']
    try:
        data = coll.insert_one({
            constant.USER_NAME: username,
            constant.PASSWORD: password,
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
