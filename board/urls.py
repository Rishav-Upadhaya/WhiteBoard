from django.urls import path
from .views import whiteboard_view

urlpatterns = [
    path('<str:room_name>/', whiteboard_view, name='whiteboard'),
]
