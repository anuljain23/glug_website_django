from django.shortcuts import render
from users import views
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
def index(request):
    return HttpResponseRedirect('/users')
