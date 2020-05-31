import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from dog.models import Dog


def current_datetime(request):
    # now = datetime.datetime.now()
    # html = "<html><body>It is now %s.</body></html>" % now
    # print("hey i am coming.")\\

    # request.get(name)
    # dogs = Dog.objects.filter().all()
    # print(dogs)
    # dog_str = ""
    # for dog in dogs:
    #     dog_str += "<br> name:" + dog.name + " weight:" + str(dog.weight)
    # html = "<html><body>%s.</body></html>" % (dog_str,)
    # return HttpResponse(html)

    return render(request, template_name="index2.html")


def post_dog(request):
    print(request.body)

    # body_unicode = request.body.decode('utf-8')
    body = json.loads(request.content)
    print(body)
    f_name = body.get('fname')
    l_name = body.get('lname')
    html = "<html><body>%s %s</body></html>" % (f_name, l_name,)
    return HttpResponse(html)

