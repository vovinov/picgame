from django.shortcuts import render


def render_site(request):
    '''Функция, отвечает за рендер сайта'''
    return render(request, 'games/game.html')


