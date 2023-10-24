from django.shortcuts import render

from data import questions


def render_questions(request):
    return render(request, 'questions/question.html', context={"movies": questions})
