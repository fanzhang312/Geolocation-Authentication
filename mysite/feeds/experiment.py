# Create your views here.
#from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse



def index(request):
    # return HttpResponse(status, mimetype="application/json")
    return render_to_response('GisProject/example.htm')


