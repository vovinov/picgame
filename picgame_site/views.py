from django.shortcuts import render


# Create your views here.
def render_home(request):
    '''Функция, отвечает за рендер первой страницы сайта'''
    return render(request, 'pages/home.html')