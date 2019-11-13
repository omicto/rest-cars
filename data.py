from pymongo import MongoClient

def get_database(database_name):
    client = MongoClient('localhost', 27017)
    return client[database_name]

db = get_database('autos')

def insert_car(car):
    db.cars.insert(car.as_dict())

def get_all_cars():
    return db.cars.find()

def get_one_car(car):
    search = car.as_dict()
    del search['details']
    return db.cars.find_one(search)

def update_car(id, new_info):
    db.cars.update({'id': id}, {'$set':new_info.as_dict()})

def delete_car(id):
    db.cars.remove({"id" : id})

#######
def insert_maker(maker):
    db.makers.insert(maker.as_dict())

def get_all_makers():
    return db.makers.find()

def get_one_maker(maker):
    search = maker.as_dict()
    del search['models']
    return db.makers.find_one(search)

def update_maker(id, new_info):
    db.makers.update_one({'id': id}, {'$set': new_info.as_dict()})