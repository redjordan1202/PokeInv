from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate
from pokemontcgsdk import *
from pokemontcgsdk import Card as card
from cards.models import Card
from django.contrib.auth.forms import UserCreationForm
from collection.forms import CollectionItemForm

# Create your views here.

def Index(request):
    return render(request, 'pages/index.html')


def Results(request):
    context = {}
    if ":" in request.GET['search']:
        s = request.GET['search'].partition(":")

        match s[0]:
            case "set":
                queryset = Card.objects.filter(sets__name__icontains='%s'%s[2]).order_by("number")
            case "set_exact":
                queryset = Card.objects.filter(sets__name='%s'%s[2]).order_by("number")
        search = s[2]
    else:
        queryset = Card.objects.filter(name__icontains=request.GET['search']).order_by("number")
        search = request.GET['search']

    form = CollectionItemForm()
    for item in queryset:
        print(item.number)

    context = {
        'cards' : queryset,
        'search' : search,
        'form' : form,
    }
    return render(request, 'pages/results.html', context)

