import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://neighborly-app-cosmos-db:gZbivkW7AY50ZSEX32bQv40nTWWGqubWQ4WUmsRHEUAJm9vGs3YUJ7sKEWc0J1fR7hFwNZUCsxOmqIjAix2uKw==@neighborly-app-cosmos-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-app-cosmos-db@"  
            client = pymongo.MongoClient(url)
            database = client['neighborly-app-db']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
