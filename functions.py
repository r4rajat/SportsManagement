import constant
from config import mongo
from bson.objectid import ObjectId


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
            constant.SPORT: sport,
            constant.REGISTRATIONS: []
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
            constant.GROUND: ground,
            constant.REGISTRATIONS: 0
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


def get_event(_id):
    _id = ObjectId(_id)
    db = mongo['sports-management']
    coll = db['events']
    try:
        event = coll.find_one({
            constant.ID: _id
        })
    except Exception as e:
        return Exception(e)

    return event


def update_event(_id, category, timing, ground, registrations=None):
    _id = ObjectId(_id)
    db = mongo['sports-management']
    coll = db['events']
    _filter = {
        constant.ID: _id
    }
    if registrations:
        new_values = {"$set": {
            constant.CATEGORY: category,
            constant.TIMING: timing,
            constant.GROUND: ground,
            constant.REGISTRATIONS: registrations
        }}
    else:
        new_values = {"$set": {
            constant.CATEGORY: category,
            constant.TIMING: timing,
            constant.GROUND: ground
        }}
    try:
        updated = coll.update_one(_filter, new_values)
    except Exception as e:
        return Exception(e)

    if updated is not None:
        return True
    else:
        return False


def delete_event(_id):
    _id = ObjectId(_id)
    db = mongo['sports-management']
    coll = db['events']
    try:
        deleted = coll.delete_one({
            constant.ID: _id
        })
    except Exception as e:
        return Exception(e)

    if deleted is not None:
        return True
    else:
        return False


def get_all_events_of_category(category):
    db = mongo['sports-management']
    coll = db['events']
    try:
        events = coll.find({
            constant.CATEGORY: category
        })
    except Exception as e:
        return Exception(e)

    all_events = []
    for event in events:
        event[constant.ID] = str(event[constant.ID])
        all_events.append(event)

    return all_events


def get_user_details(user_id):
    db = mongo['sports-management']
    coll = db['users']
    try:
        user = coll.find_one({
            constant.USER_NAME: user_id
        })
    except Exception as e:
        return Exception(e)

    if user is not None:
        return user
    else:
        return None


def update_user_details(user_id, full_name, password, email, gender, age, sport, registrations=None):
    db = mongo['sports-management']
    coll = db['users']
    _filter = {
        constant.USER_NAME: user_id
    }
    if registrations:
        new_values = {"$set": {
            constant.PASSWORD: password,
            constant.FULL_NAME: full_name,
            constant.EMAIL: email,
            constant.GENDER: gender,
            constant.AGE: age,
            constant.SPORT: sport,
            constant.REGISTRATIONS: registrations
        }}
    else:
        new_values = {"$set": {
            constant.PASSWORD: password,
            constant.FULL_NAME: full_name,
            constant.EMAIL: email,
            constant.GENDER: gender,
            constant.AGE: age,
            constant.SPORT: sport
        }}

    try:
        updated = coll.update_one(_filter, new_values)
    except Exception as e:
        return Exception(e)

    if updated is not None:
        return True
    else:
        return False


def register_user_to_event(user_id, event_id):
    _event_id = ObjectId(event_id)
    event_details = get_event(_event_id)

    user_detials = get_user_details(user_id)
    user_registrations = user_detials[constant.REGISTRATIONS]
    alreadyRegistered = False
    if len(user_registrations) != 0:
        for reg in user_registrations:
            if reg[constant.ID] == _event_id:
                alreadyRegistered = True
                break

    if not alreadyRegistered:
        update_event(_id=event_id,
                     category=event_details[constant.CATEGORY],
                     timing=event_details[constant.TIMING],
                     ground=event_details[constant.GROUND],
                     registrations=event_details[constant.REGISTRATIONS] + 1
                     )

        user_registrations.append(event_details)
        update_user_details(
            user_id=user_id,
            full_name=user_detials[constant.FULL_NAME],
            password=user_detials[constant.PASSWORD],
            email=user_detials[constant.EMAIL],
            gender=user_detials[constant.GENDER],
            age=user_detials[constant.AGE],
            sport=user_detials[constant.SPORT],
            registrations=user_registrations
        )
