from flask_restful import Resource, reqparse
import data as db
import json
from bson.json_util import dumps

car_parser = reqparse.RequestParser()
car_parser.add_argument('id')
car_parser.add_argument('model')
car_parser.add_argument('descr')

class CarList(Resource):
    def get(self):
        return json.loads(dumps(db.get_all_cars()))

    def post(self):
        args = car_parser.parse_args()
        car = Car(int(args["id"]), args["model"], args["descr"])
        db.insert_car(car)
        return car.as_dict()

class CarResource(Resource):
    def get(self, car_id):
        return json.loads(dumps(db.get_one_car(Car(id=int(car_id)))))
        
    def delete(self, car_id):
        car_id = int(car_id)
        car = self.get(car_id)
        db.delete_car(car_id)
        return car

    def put(self, car_id):
        car_id = int(car_id)
        args = car_parser.parse_args()
        car = Car(int(args["id"]), args["model"], args["descr"])
        db.update_car(car_id, car)
        return car.as_dict()

class Car:
    def __init__(self, id = None, model = None, descr = None, details = None):
        self._id = id
        self._model = model
        self._descr = descr
        self._details = details

    def as_dict(self):
        details = self._details.as_dict() if self._details is not None else None
        d = {
            "details" : details
        }
        if self._id is not None: d["id"] = self._id
        if self._model is not None: d["model"] = self._model
        if self._descr is not None: d["descr"] = self._descr
        return d

class Details:
    def __init__(self, cylinders, edispl, weight, accel, year,mpg, horsepower):
        self._cylinders
        self._edispl
        self._weight
        self._accel
        self._year
        self._mpg
        self._horsepower

    def as_dict(self):
        d = {
            "cylinders": self._cylinders,
            "edispl": self._edispl,
            "weight": self._weight,
            "accel": self._accel,
            "year": self._year,
            "mpg": self._mpg,
            "horsepower": self._horsepower
        }
        return d