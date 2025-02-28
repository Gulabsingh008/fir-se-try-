import os
from pymongo import MongoClient

# MongoDB कनेक्शन
DATABASE_URI = os.getenv("DATABASE_URI", "")
DATABASE_NAME = "techvjclonefilterbot"
COLLECTION_NAME = "vjcollection"

client = MongoClient(DATABASE_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]  # ✅ अब collection यहां पर सेट हो गया है
