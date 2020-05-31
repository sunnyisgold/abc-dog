from datetime import datetime
from random import randint

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from dog.models import Dog


def current_datetime(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # print("hey i am coming.")\\

    # request.get(name)
    random_str = randint(0,100)
    abc = "dog's name: {}".format(random_str)

    dog = Dog.objects.create(name=random_str, weight=100)
    return render(request, template_name="index.html", context={'abc': dog.name})