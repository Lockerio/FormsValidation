import os
import pymongo


db_client = pymongo.MongoClient(os.getenv('DB_URL'))
db = db_client[os.getenv('DB_NAME')]
