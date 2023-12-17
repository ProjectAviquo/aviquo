"""API models"""
import json

from django.db import models


class Message(models.Model):
    "Chat message model"
    content = models.TextField()
    # TODO: we'd sync this up somehow once the website is ready
    # sender = models.ForeignKey(User, on_delete=models.CASCADE)
    sender = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return as str"""
        return f"Message from {self.sender} at {self.timestamp}"

    def to_json_dict(self):
        """Return as string json"""
        return json.dumps(
            {
                "sender": self.sender,
                "text": self.content,
            }
        )
