from django.db import models
from django.contrib.auth.models import User


class Issue(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True , related_name='issues')

    def __str__(self):
        return self.title