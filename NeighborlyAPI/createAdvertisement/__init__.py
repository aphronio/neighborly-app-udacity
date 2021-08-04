import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://neighborly-app-cosmos-db:gZbivkW7AY50ZSEX32bQv40nTWWGqubWQ4WUmsRHEUAJm9vGs3YUJ7sKEWc0J1fR7hFwNZUCsxOmqIjAix2uKw==@neighborly-app-cosmos-db.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@neighborly-app-cosmos-db@"  
            client = pymongo.MongoClient(url)
            database = client['neighborly-app-db']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )