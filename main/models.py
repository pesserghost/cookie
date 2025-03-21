from django.db import models

# Create your models here.
from django.http import HttpResponse, HttpRequest


def set_value_in_cookie(request):
    response = HttpResponse('<h1> Salom Dunyo </h1>')
    response.set_cookie('name', 'Toxir', expires=3600)
    return  response

def get_value_from_cookie(request: HttpRequest):
    name = request.COOKIES.get('name')
    session_id = request.COOKIES.get('sessionid')
    csrftoken = request.COOKIES.get('csrftoken')
    return HttpResponse(f'<h1><b>name:</b> {name}<br><b>session_id:</b> {session_id}<br><b>csrftoken:</b> {csrftoken}</h1>')



def update_value_in_cookie(request):
    response = HttpResponse('<h1> Salom Dunyo </h1>')
    response.set_cookie('name', 'Sobir', expires=3600)
    return  response



def delete(request):
    response = HttpResponse("O'chirildi!!!")
    response.delete_cookie("name")
    return response