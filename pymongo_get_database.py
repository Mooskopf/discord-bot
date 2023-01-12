from pymongo import MongoClient
import os
from dotenv import load_dotenv

def get_database():
   
   load_dotenv()
   USER = os.getenv('USER')
   PASSWORD = os.getenv('PASSWORD')

   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://" + USER + ":" + PASSWORD + "@floscluster.6iajehp.mongodb.net/?retryWrites=true&w=majority"
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
   
   return client['BushalteDB']