import time
from pymongo import MongoClient

client = MongoClient("mongodb://mongo:27017")
db = client["expense_db"]
collection = db["expenses"]

while True:
    pending = collection.find({"status": "pending"})

    for item in pending:
        print("Processing", item["title"])

        collection.update_one(
            {"_id": item["_id"]},
            {"$set": {"status": "done"}}
        )

    time.sleep(5)
