from pyrogram import Client, filters
from pymongo import MongoClient
from info import DATABASE_URI, DATABASE_NAME, COLLECTION_NAME  # Import from info.py
import random

# MongoDB से कनेक्ट करें
mongo_client = MongoClient(DATABASE_URI)
db = mongo_client[DATABASE_NAME]
users_collection = db["users"]
files_collection = db[COLLECTION_NAME]  # Collection का नाम info.py से

@Client.on_message(filters.command("today"))
async def today_handler(client, message):
    user_id = message.from_user.id
    
    # यूज़र का डेटा निकालें
    user_data = users_collection.find_one({"user_id": user_id})
    
    if not user_data:
        await message.reply("⚠️ आप रजिस्टर नहीं हैं! पहले /start दबाएँ।")
        return

    is_premium = user_data.get("is_premium", False)
    daily_limit = user_data.get("daily_limit", 0)
    max_limit = 15 if is_premium else 3  # प्रीमियम = 15, फ्री = 3

    if daily_limit >= max_limit:
        await message.reply("⚠️ आज की लिमिट समाप्त हो गई है! कृपया कल पुनः प्रयास करें।")
        return

    # चेक करें कि फाइल्स उपलब्ध हैं या नहीं
    total_files = files_collection.count_documents({})
    if total_files == 0:
        await message.reply("⚠️ कोई फाइल उपलब्ध नहीं है!")
        return

    # रैंडम फाइल भेजें
    random_index = random.randint(0, total_files - 1)
    random_file = files_collection.find().skip(random_index).limit(1)[0]

    if not random_file:
        await message.reply("⚠️ कोई फाइल नहीं मिली!")
        return

    file_id = random_file["file_id"]
    await message.reply_document(document=file_id, caption="🎁 Here is your file!")

    # यूज़र की डेली लिमिट अपडेट करें
    users_collection.update_one({"user_id": user_id}, {"$inc": {"daily_limit": 1}})
