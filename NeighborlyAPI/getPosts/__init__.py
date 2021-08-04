import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://neighborly-app-cosmos-db:gZbivkW7AY50ZSEX32bQv40nTWWGqubWQ4WUmsRHEUAJm9vGs3YUJ7sKEWc0J1fR7hFwNZUCsxOmqIjAix2uKw==@neighborly-app-cosmos-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-app-cosmos-db@"  
        client = pymongo.MongoClient(url)
        database = client['neighborly-app-db']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)