from flask import Flask, jsonify
from flask_restful import Api, Resource
import new_grad
import swe_internship

app = Flask(__name__)
api = Api(app)

class New_Grad_Jobs(Resource):
    def get(self):
        return_JSON = new_grad.new_grad_jobs()
        return jsonify(return_JSON)

class Swe_Internship_Jobs(Resource):
    def get(self):
        return_JSON = swe_internship.swe_internship()
        return jsonify(return_JSON)

api.add_resource(New_Grad_Jobs, "/new_grad")
api.add_resource(Swe_Internship_Jobs, "/internship")


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)