import pymongo
from config import CONNECTION_STRING

client = pymongo.MongoClient(CONNECTION_STRING)
database = client.geekstat

