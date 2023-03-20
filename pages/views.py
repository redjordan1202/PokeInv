from django.shortcuts import render, HttpResponse
from pokemontcgsdk import *
from pokemontcgsdk import Card as card
from cards.models import Card

# Create your views here.

def Index(request):
    return render(request, 'pages/index.html')


def Results(request):
    context = {}
    if ":" in request.GET['search']:
        print(request.GET['search'])
        search = request.GET['search']
        print(search)
        s = search.partition(":")
        print(s)

        match s[0]:
            case "set":
                print("set")
                print(s[2])
                queryset = Card.objects.filter(sets__name__icontains='%s'%s[2])
            case "set_exact":
                print("set")
                print(s[2])
                queryset = Card.objects.filter(sets__name='%s'%s[2])
    else:
        print(request.GET['search'])
        queryset = None

    context = {
        'cards' : queryset,
        'search' : request.GET['search']
    }
    return render(request, 'pages/results.html', context)