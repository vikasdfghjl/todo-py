from bson.objectid import ObjectId
from datetime import datetime

class Task:
    def __init__(self, content, created_at=None, completed=False):
        self.content = content
        self.completed = completed
        self.created_at = created_at if created_at is not None else datetime.now()  # Set created_at to now if not provided
        self.id = ObjectId()  # Automatically generate a new ObjectId for new tasks

    def to_dict(self):
        """Convert the Task object to a dictionary."""
        return {
            "_id": self.id,  # Store the ObjectId
            "content": self.content,
            "completed": self.completed,
            "created_at": self.created_at  # Store the created_at date
        }

    @staticmethod
    def from_dict(data):
        """Create a Task object from a dictionary."""
        created_at = data.get("created_at", datetime.now())  # Use current time if missing
        task = Task(
            content=data["content"],
            completed=data.get("completed", False),
            created_at=created_at  # Correctly pass created_at
        )
        task.id = str(data["_id"])  # Convert ObjectId to string
        return task
