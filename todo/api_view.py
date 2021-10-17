from todo.models import Todo
from .serializers import TodoSerializer
from rest_framework import viewsets
from todo.serializers import TodoSerializer

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()