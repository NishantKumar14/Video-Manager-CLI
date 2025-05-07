from pymongo import MongoClient
from dotenv import load_dotenv
from bson import ObjectId
import os

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URL")

if not MONGODB_URI:
    raise ValueError("No MONGODB_URI found in enviroment variables.")


try:
    client = MongoClient(MONGODB_URI)

    db = client["videoManager"]
    video_collection = db["videos"]

    print(video_collection)
except Exception as e:
    print("Failed to connect MongoDB: {e}")
    raise


def list_all_video():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {'$set': {"name": new_name, "time": new_time}}
    )

def delete_video(video_id):
    video_collection.delete_one({'_id': ObjectId(video_id)})


def main():
    while True:
        print("\n Video Manager app(CLI) with MongoDB")
        print("1. List videos")
        print("2. Add a new video")
        print("3. Update a videos")
        print("4. Delete a videos")
        print("5. Exit app")

        choice = input("\n Enter your choice: ")
        
        match choice:
            case '1':
                list_all_video()
                
            case '2':
                name = input("Enter a video name: ")
                time = input("Enter a video time: ")
                add_video(name, time)

            case '3':
                video_id = input("Enter a video ID to update: ")
                name = input("Enter a video name to update: ")
                time = input("Enter a video time to update: ")
                update_video(video_id, name, time)

            case '4':
                video_id = input("Enter a video ID to delete: ")
                delete_video(video_id)

            case '5':
                break

            case _:
                print("Invalid Choice.")

    client.close()


if __name__ == "__main__":
    main()
