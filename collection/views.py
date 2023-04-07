from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.core import serializers
from .models import Collection, CollectionItem
from .forms import CollectionItemForm
from cards.models import Card
from django.contrib.auth.decorators import login_required
import json


# Create your views here.

def CollectionView(request):
    if request.user.is_authenticated:
        try:
            collection = Collection.objects.get(user = request.user)
        except:
            collection = Collection(user = request.user).save()
        items = collection.collectionitem_set.all()
        if items:
            context = {'items':items}
            print(items)
        else:
            context = {'items':None}
        return render(request, 'collection/collectionView.html', context)
    else:
        redirect("login")

def ajaxAddCardView(request):
    data = {}
    if request.user.is_authenticated:
        data["authenticated"] = True
    else:
        data["authenticated"] = False

    if  request.headers.get('x-requested-with') == 'XMLHttpRequest' and request.method == "POST":
        form = CollectionItemForm(request.POST)
        if form.is_valid():
            item = CollectionItem()
            card = Card.objects.get(id = form.cleaned_data.get('card'))
            item.card = card
            item.quantity = form.cleaned_data.get('quantity')
            item.collection = Collection.objects.get(user = request.user)
            item.save()
            data["status"] = True
        else:
            data["status"] = False
    else:
        print("Somehow not an AJAX request")

    jsonr = json.dumps(data)
    return HttpResponse(jsonr, content_type='application/json')
