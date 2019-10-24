from django.shortcuts import render

from django.http import HttpResponse, HttpRequest

from .models import User


def index(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'home/index.html',
        {
            'usernames': User.objects.all()
        }
    )
