from django.shortcuts import render, HttpResponse
from django.core import serializers
from pokemontcgsdk import *
from pokemontcgsdk import Card as card
from decouple import config
from .models import Card
import json


RestClient.configure(config("API_Key"))

# Create your views here.

def CardView(request, card_id):
    if Card.objects.filter(id = card_id):
        current_card = Card.objects.get(id = card_id)
    else:
        current_card = card.find(card_id)
        parseCardInfo(current_card)
        current_card = Card.objects.get(id = card_id)
    
    context = {'card' : current_card}

    return render(request, 'card/CardView.html', context)






def parseCardInfo(card):
    new_card =  Card(id = card.id)

    if card.abilities:
        abilities = {
            "name" : card.abilities[0].name,
            "text" : card.abilities[0].text,
            "type" : card.abilities[0].type
        }
    else:
        abilities = {
            "name" : None,
            "text" : None,
            "type" : None
        }
    new_card.abilities = abilities


    if card.artist:
        new_card.artist = card.artist
    else:
        new_card.artist = None


    if card.ancientTrait:
        ancientTrait = {
            "name" : card.ancientTrait.name,
            "text" : card.ancientTrait.text,
        }
    else:
        ancientTrait = {
            "name" : None,
            "text" : None,
        }
    new_card.ancientTrait = ancientTrait

    attacks = {
            'attack1' : None,
            'attack2' : None,
            'attack3' : None,
            'attack4' : None,
    }
    
    if card.attacks:
        i = 1
        for attack in card.attacks:
            atk = {
                'name' : attack.name,
                'cost' : attack.cost,
                'convertedEnergyCost' : attack.convertedEnergyCost,
                'damage' : attack.damage,
                'text' : attack.text,
            }
            attacks["attack%i"%i] = atk
            i = i+1
        new_card.attacks = attacks

    new_card.convertedRetreatCost = card.convertedRetreatCost
    new_card.evolvesFrom = card.evolvesFrom
    new_card.flavorText = card.flavorText
    new_card.hp = card.hp


    images = {
        'small': card.images.small,
        'large' : card.images.large
    }
    new_card.images = images

    legalities = {
        'unlimited' : card.legalities.unlimited,
        'expanded' : card.legalities.expanded,
        'standard' : card.legalities.standard,
    }
    new_card.legalities = legalities

    new_card.regulationMark = card.regulationMark
    new_card.name = card.name

    dex_numbers = {
        'number1' : None,
        'number2' : None,
        'number3' : None,
    }

    i = 1
    if card.nationalPokedexNumbers:
        for number in card.nationalPokedexNumbers:
            dex_numbers['number%i' % i] = number
            i = i+1
        new_card.nationalPokedexNumbers = dex_numbers
    else:
        new_card.nationalPokedexNumbers = None

    new_card.number = card.number
    new_card.rarity = card.rarity

    if card.resistances:
        resistances = {
            'type' : card.resistances[0].type,
            'value' : card.resistances[0].value
        }
        new_card.resistances = resistances
    else:
        new_card.resistances = None

    retreat_cost = {
        'type1' : None,
        'type2' : None,
        'type3' : None,
        'type4' : None,
        'type5' : None,
    }

    if card.retreatCost:
        i = 1
        for energy in card.retreatCost:
            retreat_cost['type%i' % i] = energy
            i = i + 1
    new_card.retreatCost = retreat_cost
    
    if card.rules:
        rules = {}
        for count, rule in enumerate(card.rules):
            rules["rule%i" % count] = rule
    else:
        rules = {}
    new_card.rules = rules

    cardSet = {
        "id" : card.set.id,
        "name" : card.set.name,
        "symbol" : card.set.images.symbol,
    }
    new_card.sets = cardSet

    if card.subtypes:
        subtypes = {}
        for count, subtype in enumerate(card.subtypes):
            subtypes["subtype%i" % count] = subtype
        new_card.subtypes = subtypes
    else:
        new_card.subtypes = None

    new_card.supertype = card.supertype
    
    if card.tcgplayer:
        tcgplayer = {
            'url' : card.tcgplayer.url,
            'updatedAt' : card.tcgplayer.updatedAt,
        }
        price = {
            'normal' : None,
            'holofoil' : None,
            'reverseHolofoil' : None,
            'firstEditionHolofoil' : None,
            'firstEditionNormal' : None,
        }

        if card.tcgplayer.prices.normal:
            price['normal'] = {
                'low' : card.tcgplayer.prices.normal.low,
                'mid' : card.tcgplayer.prices.normal.mid,
                'high' : card.tcgplayer.prices.normal.high,
                'market' : card.tcgplayer.prices.normal.market,
                'directLow' : card.tcgplayer.prices.normal.directLow,
            }
        
        if card.tcgplayer.prices.holofoil:
            price['holofoil'] = {
                'low' : card.tcgplayer.prices.holofoil.low,
                'mid' : card.tcgplayer.prices.holofoil.mid,
                'high' : card.tcgplayer.prices.holofoil.high,
                'market' : card.tcgplayer.prices.holofoil.market,
                'directLow' : card.tcgplayer.prices.holofoil.directLow,
            }

        if card.tcgplayer.prices.reverseHolofoil:
            price['reverseHolofoil'] = {
                'low' : card.tcgplayer.prices.reverseHolofoil.low,
                'mid' : card.tcgplayer.prices.reverseHolofoil.mid,
                'high' : card.tcgplayer.prices.reverseHolofoil.high,
                'market' : card.tcgplayer.prices.reverseHolofoil.market,
                'directLow' : card.tcgplayer.prices.reverseHolofoil.directLow,
            }

        if card.tcgplayer.prices.firstEditionHolofoil:
            price['firstEditionHolofoil'] = {
                'low' : card.tcgplayer.prices.firstEditionHolofoil.low,
                'mid' : card.tcgplayer.prices.firstEditionHolofoil.mid,
                'high' : card.tcgplayer.prices.firstEditionHolofoil.high,
                'market' : card.tcgplayer.prices.firstEditionHolofoil.market,
                'directLow' : card.tcgplayer.prices.firstEditionHolofoil.directLow,
            }

        if card.tcgplayer.prices.firstEditionNormal:
            price['firstEditionNormal'] = {
                'low' : card.tcgplayer.prices.firstEditionNormal.low,
                'mid' : card.tcgplayer.prices.firstEditionNormal.mid,
                'high' : card.tcgplayer.prices.firstEditionNormal.high,
                'market' : card.tcgplayer.prices.firstEditionNormal.market,
                'directLow' : card.tcgplayer.prices.firstEditionNormal.directLow,
            }
        tcgplayer["prices"] = price
    else:
        tcgplayer = {}
    new_card.tcgplayer = tcgplayer

    if card.types:
        types = {
            "type1" : None,
            "type2" : None
        }
        i = 1
        for x in card.types:
            print(x)
            types["type%i" % i] = x
            i = i + 1
        new_card.types = types
    else:
        new_card.types = None

    if card.weaknesses:
        weakness = {
            'type' : card.weaknesses[0].type,
            'value' : card.weaknesses[0].value
        }
        new_card.weaknesses = weakness
    else:
        new_card.weaknesses = None

    new_card.save()


