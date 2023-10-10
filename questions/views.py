from django.shortcuts import render


def render_questions(request):
    return render(request, 'questions/index.html')
