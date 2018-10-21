from flask import Flask, render_template
from flask_restful import Api, Resource, reqparse
import json

app = Flask(__name__)
api = Api(app)

# users = [
#     {
#         "name" : "Nicolas",
#         "age": 42,
#         "occupation": "Network Eng"
#     },
#     {
#         'name' : 'Evan',
#         'age': 29,
#         "occupation": "CS Eng"
#     },
#     {
#         "name" : "Jess",
#         "age": 35,
#         "occupation": "Bikar"
#     }
#     ]

class DB(Resource):
    def get(self, name):
        # for user in users:
        #     if(name == user["name"]):
        #         return user, 200
        # return "user not found", 404
        return "this is a test get request", 200

    def post(self, name):
        # parser = reqparse.RequestParser()
        # parser.add_argument("age")
        # parser.add_argument("occupation")
        # args = parser.parse_args()

        # for user in users:
        #     if(name == user["name"]):
        #         return "User with name {} already exists".format(name), 400

        # user = {
        #     "name": name,
        #     "age": args["age"],
        #     "occupation": args["occupation"]
        # }
        # users.append(user)
        # return user, 201
        return "this is a test post request", 201

    def put(self, name):
        # parser = reqparse.RequestParser()
        # parser.add_argument("age")
        # parser.add_argument("occupation")
        # args = parser.parse_args()

        # for user in users:
        #     if(name == user["name"]):
        #         user["age"] = args["age"]
        #         user["occupation"] = args["occupation"]
        #         return user, 200

        # user = 
        #     "name": name,
        #     "age": args["age"],
        #     "occupation": args["occupation"]
        # }
        # users.append(user)
        # return user, 201
        return "this is a test put request", 200

    def delete(self, name):
        # global users
        # users = [user for user in users if user["name"] != name]
        # return "{} is deleted".format(name), 200
        return "this is a test delete request", 200

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    jsonFile = open('app.json')
    jsonText = jsonFile.read()
    json_data = json.loads(jsonText)

    ##card 1
    date = json_data[0]['launchStart']
    name = json_data[0]['name']
    mission = json_data[0]['mission']
    company = json_data[0]['lspname']
    location = json_data[0]['location']
    

    ##card 2
    date2 = json_data[1]['launchStart']
    name2 = json_data[1]['name']
    mission2 = json_data[1]['mission']
    company2 = json_data[1]['lspname']
    location2 = json_data[1]['location']

    ##card 3
    date3 = json_data[2]['launchStart']
    name3 = json_data[2]['name']
    mission3 = json_data[2]['mission']
    company3 = json_data[2]['lspname']
    location3 = json_data[2]['location']
    

    return render_template('home.html', date=date, name=name, mission=mission, company=company, location=location,
                                        date2=date2, name2=name2, mission2=mission2, company2=company2, location2=location2,
                                        date3=date3, name3=name3, mission3=mission3, company3=company3, location3=location3)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/get', methods=['GET'])
def getDB():
    # pollutionJson = getFromDB('pollutionInfo')
    # return pollutionJson
    return 'Success GET', 999

@app.route('/launch')
def launch():
    return render_template('launch.html')

# if __name__ == '__main__':
# 	app.run(debug=True)