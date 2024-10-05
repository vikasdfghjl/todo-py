import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
from bson import ObjectId
from models import Task

# Load environment variables from .env file
load_dotenv()

# MongoDB connection
mongo_uri = os.getenv('MONGO_URI')

try:
    client = MongoClient(mongo_uri)
    # Attempt to access the database to check connection
    client.admin.command('ping')  # This command will ping the server
    print("MongoDB connection successful.")
except ConnectionFailure:
    print("MongoDB connection failed. Please check your connection string and credentials.")
    client = None  # Set client to None if the connection failed

# Define the database and collection only if the client is successfully created
if client:
    db = client.taskdb  # Replace 'taskdb' with your database name
    tasks_collection = db.tasks  # Collection to store tasks
else:
    db = None
    tasks_collection = None

def get_tasks():
    """Retrieve all tasks from the database."""
    if tasks_collection is not None:
        try:
            tasks = tasks_collection.find()
            return [Task.from_dict(task) for task in tasks]  # Convert to Task instances
        except Exception as e:
            print(f"Error retrieving tasks: {e}")
            return []
    else:
        print("Database connection is not established.")
        return []

def add_task(content, created_at):
    """Add a new task to the database."""
    if tasks_collection is not None:
        task = Task(content, created_at)  # Create a new Task instance
        task_dict = task.to_dict()  # Convert the Task instance to a dictionary

        # Add the completed field explicitly as False
        task_dict["completed"] = False  

        # Insert the task into the database
        tasks_collection.insert_one(task_dict)
  # Store it in the database

def update_task(task_id, completed):
    """Update a task's completion status in the database."""
    if tasks_collection is not None:
        tasks_collection.update_one({"_id": ObjectId(task_id)}, {"$set": {"completed": completed}})


def delete_task(task_id):
    """Delete a task from the database."""
    if tasks_collection is not None:
        tasks_collection.delete_one({"_id": ObjectId(task_id)})
