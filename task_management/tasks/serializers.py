from rest_framework import serializers
from .models import User, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'mobile']


class TaskSerializer(serializers.ModelSerializer):
    assigned_users = UserSerializer(many=True, read_only=True)  # Nested serializer

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'created_at', 'completed_at', 'task_type', 'status', 'assigned_users']

class TaskAssignSerializer(serializers.ModelSerializer):
    assigned_users = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all())

    class Meta:
        model = Task
        fields = ['assigned_users']
