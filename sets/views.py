from django.shortcuts import render, HttpResponse
from pokemontcgsdk import *
from decouple import config
from .models import Card_Set
import datetime
# Create your views here.

def SetsView(request):
    queryset = Card_Set.objects.all().order_by('-releaseDate')

    context = {
        "series" : {},
    }

    for item in queryset:
        if item.series in context['series'].keys():
            context['series'][item.series].append(item)
        else:
            context['series'][item.series] = []
            context['series'][item.series].append(item)

    return render(request, "sets/SetsView.html", context)

def ImportSets(request):
    sets = Set.all()
    sets_imported = 0
    for x in sets:
        if Card_Set.objects.filter(id = x.id):
            continue
        else:
            new_set = Card_Set(id = x.id)

            if x.images:
                images = {
                    'symbol' : x.images.symbol,
                    'logo'  : x.images.logo
                }
                new_set.images = images
            else:
                new_set.images = None

            if x.legalities:
                legalities = {
                    'unlimited' : x.legalities.unlimited,
                    'expanded' : x.legalities.expanded,
                    'standard' : x.legalities.standard, 
                }
                new_set.legalities = legalities
            else:
                new_set.legalities = None

            new_set.name = x.name
            new_set.printedTotal = x.printedTotal
            new_set.ptcgoCode = x.ptcgoCode

            date_format = '%Y/%m/%d'
            released = datetime.datetime.strptime(x.releaseDate, date_format)
            new_set.releaseDate = released

            new_set.series = x.series
            new_set.total = x.total

            new_set.save()
            sets_imported = sets_imported+1

    return HttpResponse('Import Complete | %i sets imported' % sets_imported)
