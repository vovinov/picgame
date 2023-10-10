from django.shortcuts import render

from data import questions


def render_questions(request):
    return render(request, 'questions/index.html', context={"movies": questions})
