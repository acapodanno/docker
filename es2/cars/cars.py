from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Cars(Resource):
    def get(self):
        return {"message": "GET successful"}, 200, {"x-custom-version": "1.0"}

    def put(self):
        return {"message": "PUT successful"}, 201, {"x-custom-version": "1.0"}

    def post(self):
        return {"message": "POST successful"}, 200, {"x-custom-version": "2.1"}


api.add_resource(Cars, "/cars")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
