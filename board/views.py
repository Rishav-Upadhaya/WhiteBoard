from django.shortcuts import render

def home_view(request):
    return render(request, "board/home.html")

def whiteboard_view(request, room_name):
    return render(request, 'board/whiteboard.html', {'room_name':room_name})
