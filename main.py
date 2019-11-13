from flask import Flask
from flask_restful import Api
from car import CarResource, CarList, CarDetails
from maker import MakerResource, MakerList

app = Flask(__name__)
api = Api(app)
api.add_resource(CarList, '/cars')
api.add_resource(CarResource, '/cars/<car_id>')
api.add_resource(CarDetails, '/cars/<car_id>/details')
api.add_resource(MakerList, '/makers')
api.add_resource(MakerResource, '/makers/<maker_id>')

if __name__ == '__main__':
    app.run(debug=True)
