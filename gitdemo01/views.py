#coding=utf-8
from django.http import HttpResponse


def index_view(reqeust):
    return HttpResponse('hello git!')