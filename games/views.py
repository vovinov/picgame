from django.shortcuts import render


def render_game(request):
    return render(request, 'games/game.html')
