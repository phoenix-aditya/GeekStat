from pymongo import MongoClient
from .database import database
from bson.objectid import ObjectId

def insert_document(
	collection_name: str,
	document : dict 
	):
	'''
	function to insert document in the collection
	'''
	collection = database[collection_name] 
	collection.insert_one(document)

def insert_documents(
	collection_name: str, 
	list_of_document: list
	):
	'''
	function to insert multiple documents in the collection
	'''
	collection = database[collection_name]
	collection.insert_many(list_of_document)


def check_if_id_in_collection(
	id: str,
	collection_name: str
	):
	'''
	function to check if a document with id present in collection
	'''
	collection = database[collection_name]
	is_present = collection.find({"_id":id}).count() > 0

	return is_present

def check_if_collection_exists(
	collection_name: str
	):
	'''
	function to check if a collection exists in the database
	'''
	list_of_collections = database.list_collection_names()
	if collection_name in list_of_collections:
		return True

	return False
 
def return_latest_doc_in_collection(
	collection_name: str
 	):
	'''
	returns the last inserted document in the
	database
	'''
	collection = database[collection_name]
	last_inserted_doc = list(collection.find().sort("_id",-1).limit(1))[0]
	return last_inserted_doc

def return_doc_by_username(
	collection_name : str,
	username : str
	):
	'''
	returns the document with the id in the
	database
	return None if document not found else the document
	'''
	collection = database[collection_name]

	query = {'username': username}
	filter = {'_id': 0}
	
	document = collection.find_one(query, filter)
	
	return document

def update_document_by_username(
	collection_name : str,
	username : str,
	document : dict
	):
	'''
	function updates the document that has the
	username set as username
	'''
	collection = database[collection_name]
	query = {'username' : username}
	updation = {'$set': document}

	collection.update_one(
		query,
		updation,
		upsert=False
	)
