from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os
import pprint

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")


connection_string = f"mongodb+srv://4midable:{password}@cluster0.adcfzoy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(connection_string)

dbs = client.list_database_names()
client_testdb = client.test_db
collections = client_testdb.list_collection_names()
print(collections )


def insert_test_doc():
	collection = client_testdb.test_db
	test_document = {
		"name": "Saheed",
		"type": "Test"
	}
	inserted_id = collection.insert_one(test_document).inserted_id
	print(inserted_id)
	
insert_test_doc()
