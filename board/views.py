from django.shortcuts import render

def whiteboard_view(request, room_name):
    return render(request, 'board/whiteboard.html', {'room_name':room_name})
