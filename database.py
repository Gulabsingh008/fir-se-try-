import os
from pymongo import MongoClient

# MongoDB कनेक्शन
DATABASE_URI = os.getenv("DATABASE_URI", "")
DATABASE_NAME = "techvjclonefilterbot"
COLLECTION_NAME = "vjcollection"

client = MongoClient(DATABASE_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# डेली लिमिट सेटिंग्स
FREE_USER_LIMIT = 3
PREMIUM_USER_LIMIT = 15
