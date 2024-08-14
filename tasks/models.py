from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name="user_tasks", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
