import os

API_ID    = os.environ.get("API_ID", "8313201920")
API_HASH  = os.environ.get("API_HASH", "3362cbcff56b786d82202086baab0bb7")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8313201920:AAH1PfXk6b6sgBPNCT_H5AEMAhZETItO5gg") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
