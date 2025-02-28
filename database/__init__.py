import os
from pymongo import MongoClient

# ✅ MongoDB कनेक्शन सेट करें
DATABASE_URI = os.getenv("DATABASE_URI", "")
DATABASE_NAME = "techvjclonefilterbot"
COLLECTION_NAME = "vjcollection"

client = MongoClient(DATABASE_URI)
db1 = client[DATABASE_NAME]
collectionss = db1[COLLECTION_NAME]  # ✅ अब सही से MongoDB कनेक्ट होगा
