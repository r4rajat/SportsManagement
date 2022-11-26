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
            return True, data
        else:
            return False, None
    else:
        return False, None


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


def add_event(category, timing, ground):
    db = mongo['sports-management']
    coll = db['events']
    try:
        inserted = coll.insert_one({
            constant.CATEGORY: category,
            constant.TIMING: timing,
            constant.GROUND: ground
        })
    except Exception as e:
        return Exception(e)

    if inserted is not None:
        return True
    else:
        return False


def get_all_events():
    db = mongo['sports-management']
    coll = db['events']
    try:
        data = coll.find({})
    except Exception as e:
        return Exception(e)

    if data is not None:
        return True, data
    else:
        return False, None
