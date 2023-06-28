import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://ahsan:SzyLkO8f0I4cCoKs@cluster0.5rskt0b.mongodb.net/")

db = cluster["test"]
collection = db["test"]

def insert_profile_image(data_dict):
    collection.insert_one(data_dict)