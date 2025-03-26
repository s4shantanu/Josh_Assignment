from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view

User = get_user_model()


@api_view(['POST'])
def create_task(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def assign_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        user_ids = request.data.get('user_ids', [])
        users = User.objects.filter(id__in=user_ids)
        task.assigned_users.set(users)
        return Response({"message": "Task assigned successfully"}, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return Response({"error": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_user_tasks(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        tasks = user.tasks.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
