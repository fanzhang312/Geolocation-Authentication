# Create your views here.
#from django.template import Context, loader
from django.shortcuts import render_to_response
from django.http import HttpResponse
import simplejson
#import httplib2
#import twitter

import tweepy
import jsonpickle


def index(request):
	# OAuth
    consumer_key='Ad3m2tX4qiwFvCEJw8HOOg'
    consumer_secret='Nzm3id4JGulXULeGVj2aiPWsxZxFvcXWuosr22D89AI'
    access_token_key='217970228-oc92QK9dInCRjuNE1dvxgPNuPC9dcvQh7uVPy5vB'
    access_token_secret='Oiru54uiWoe7GMYz59w0ykCf9IACi2s9zGRtWSWA8'
    auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
    auth.set_access_token(access_token_key,access_token_secret)
    api = tweepy.API(auth)
    
    # Get umnSUA timeline
    statuses = tweepy.Cursor(api.user_timeline,id="UMNCSE",include_rts="false",exclude_replies="true").items(20)
    # test = api.user_timeline(id="umnSUA",include_rts="false",exclude_replies="true",count=3)
    # status = jsonpickle.encode(test)
    # return HttpResponse(status, mimetype="application/json")
    return render_to_response('feeds/index.html',{'latest_feed_list':statuses})


