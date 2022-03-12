from django.http import HttpResponse
from django.shortcuts import render

def index(response):
    return HttpResponse('Hello World')
