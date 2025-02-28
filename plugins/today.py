from pyrogram import Client

@Client.on_message()
async def debug_all_messages(client, message):
    print(f"📩 Received message: {message.text}")  # Debugging
