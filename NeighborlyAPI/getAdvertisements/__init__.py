import azure.functions as func
import pymongo
import json
from bson.json_util import dumps

def main(req: func.HttpRequest) -> func.HttpResponse:

    try:
        url = "mongodb://neighborly-app-cosmos-db:gZbivkW7AY50ZSEX32bQv40nTWWGqubWQ4WUmsRHEUAJm9vGs3YUJ7sKEWc0J1fR7hFwNZUCsxOmqIjAix2uKw==@neighborly-app-cosmos-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-app-cosmos-db@"  
        client = pymongo.MongoClient(url)
        database = client['neighborly-app-db']
        collection = database['advertisements']


        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8')
    except:
        print("could not connect to mongodb")
        return func.HttpResponse("could not connect to mongodb",
                                 status_code=400)

