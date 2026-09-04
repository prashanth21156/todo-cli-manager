class Task:
    """Represent a single to-do task."""

    def __init__(self, task_id, title=None, completed=False):
        # Allow the old Task("title") form while supporting explicit IDs.
        if title is None:
            title = task_id
            task_id = None

        self.id = task_id
        self.title = title
        self.completed = completed

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def to_dict(self):
        """Return the task in the JSON storage format."""
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data):
        """Create a task from its JSON representation."""
        return cls(data["id"], data["title"], data.get("completed", False))
