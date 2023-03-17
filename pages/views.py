from django.shortcuts import render, HttpResponse
from pokemontcgsdk import *

# Create your views here.

def Index(request):
    return render(request, 'pages/index.html')


def Results(request):
    context = {}
    if request.GET['search'] != '':
        try:
            cards = Card.where(q=request.GET['search'], orderBy='+set.releaseDate')
        except:
            query = 'name:\"%s\"' % request.GET['search']
            cards = Card.where(q=query, orderBy='+set.releaseDate')
        context = {
            'cards' : cards,
            'search' : request.GET['search']
        }
    return render(request, 'pages/results.html', context)