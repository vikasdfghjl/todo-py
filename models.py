from bson.objectid import ObjectId
from datetime import datetime

class Task:
    def __init__(self, content, completed=False):
        self.content = content
        self.completed = completed
        self.created_at = datetime.now()
        self.id = ObjectId()  # Automatically generate a new ObjectId

    def to_dict(self):
        """Convert the Task object to a dictionary."""
        return {
            "_id": self.id,
            "content": self.content,
            "completed": self.completed,
            "created_at": self.created_at
        }

    @staticmethod
    def from_dict(data):
        """Create a Task object from a dictionary."""
        task = Task(content=data["content"], completed=data.get("completed", False))
        task.id = data["_id"]  # Set the id from the MongoDB document
        return task
