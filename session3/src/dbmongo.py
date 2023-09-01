from pymongo import MongoClient #pip install pymongo
#import certifi
import os

#Setear variable de entorno
#MONGO_URI = os.environ["MONGO_URI"]
MONGO_URI = "mongodb+srv://umb:XMWUynXn8vLALVna@cluster0.yzmi6hy.mongodb.net/"

#ca = certifi.where()

def dbConnection():
    try: 
        client = MongoClient(MONGO_URI)
        db = client['umb_students']
    except :
        return False
    return db

def dbinfo():
    try: 
        client = MongoClient(MONGO_URI)
        jinfo = client.server_info()
    except:
        return False
    return jinfo.get('version')
