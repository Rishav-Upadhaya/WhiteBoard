from django.urls import path
from .views import whiteboard_view, home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('<str:room_name>/', whiteboard_view, name='whiteboard'),
]
