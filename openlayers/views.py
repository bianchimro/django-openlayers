# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect

from models import *

def map(request, id):

    map = Map.objects.get(pk=id)
    
    return render_to_response("map.html", {'map' : map })
