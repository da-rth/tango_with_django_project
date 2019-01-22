from django.shortcuts import render

from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Homepage"
                        "<br>"
                        "<a href='/rango/'>Index</href>"
                        "<br>"
                        "<a href='/rango/about/'>About</href>")


def index(request):
    context_dict = {
        'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"
    }
    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'author': "2086380A"}
    return render(request, 'rango/about.html', context=context_dict)
