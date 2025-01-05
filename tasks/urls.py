from django.urls import path
from .views import TaskListCreate, TaskUpdate

urlpatterns = [
    path('', TaskListCreate.as_view(), name='task-list-create'),
    path('<int:pk>/', TaskUpdate.as_view(), name='task-update'),
]

