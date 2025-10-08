import os
from pymongo import MongoClient
from dotenv import load_dotenv

try:
    print("Loading environment vars")
    load_dotenv()
    print("Loaded environment vars\n")
except Exception as e:
    print(f"Error loading environment vars: {e}")

USER = os.getenv("MONGO_USER", "admin")
PASSWORD = os.getenv("MONGO_PASSWORD", "password")
HOST = os.getenv("MONGO_HOST", "localhost")

MONGO_URI = f"mongodb://{USER}:{PASSWORD}@{HOST}:27017/"
client = MongoClient(MONGO_URI)
db = client["auth_db"]
users_collection = db["users"]
