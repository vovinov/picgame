from django.shortcuts import render

from data import questions


def render_game(request, game_id):
    return render(request, 'questions/question.html', context={"id": game_id, "movies": questions})
