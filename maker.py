from flask_restful import Resource, reqparse
import data as db
import json
from bson.json_util import dumps

maker_parser = reqparse.RequestParser()
maker_parser.add_argument('id', type=int)
maker_parser.add_argument('fullname')
maker_parser.add_argument('maker')
maker_parser.add_argument('countryname')
maker_parser.add_argument('continent')


class MakerList(Resource):
    def get(self):
        return json.loads(dumps(db.get_all_makers()))

    def post(self):
        args = maker_parser.parse_args()
        maker = Maker(args["id"], args["maker"], args["fullname"], Location(args["countryname"], args["continent"]))
        db.insert_maker(maker)
        return maker.as_dict()

class MakerResource(Resource):
    def get(self, maker_id):
        return json.loads(dumps(db.get_one_maker(Maker(id=int(maker_id)))))
        
    def delete(self, maker_id):
        maker_id = int(maker_id)
        maker = self.get(maker_id)
        db.delete_maker(maker_id)
        return maker
    def put(self, maker_id):
        maker_id = int(maker_id)
        args = maker_parser.parse_args()
        maker = Maker(args["id"], args["maker"], args["fullname"], Location(args["countryname"], args["continent"]))
        db.update_maker(maker_id, maker)
        return maker.as_dict()

class Maker:
    def __init__(self, id = None, maker = None, fullname = None, location = None, models = None):
        self._id = id
        self._maker = maker
        self._fullname = fullname
        self._location = location
        self._models = models if models is not None else []

    def as_dict(self):
        d = {}
        if self._id is not None: d["id"] = self._id
        if self._maker is not None: d["maker"] = self._maker
        if self._fullname is not None: d["fullname"] = self._fullname
        if self._location is not None: d["location"] = self._location.as_dict()
        if self._models is not None: d["models"] = self._models
        return d
    
    def add_model(self, model):
        self._models.append(model)

class Location:
    def __init__(self, countryname, continent):
        self._countryname = countryname
        self._continent = continent

    def as_dict(self):
        d = {
            "countryname":self._countryname,
            "continent":self._continent
        }
        return d

