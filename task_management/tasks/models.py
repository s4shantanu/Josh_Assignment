from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):  
    mobile = models.CharField(max_length=15, unique=True, blank=True, null=True)
    
    groups = models.ManyToManyField(Group, related_name="custom_user_groups", blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name="custom_user_permissions", blank=True)

class Task(models.Model):
    TASK_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(null=True, blank=True)
    task_type = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=TASK_STATUS_CHOICES, default='pending')
    assigned_users = models.ManyToManyField(User, related_name="tasks")

    def __str__(self):
        return self.name
