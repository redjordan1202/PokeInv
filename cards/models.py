from django.db import models


# Create your models here.


class Card(models.Model):
    id = models.CharField(max_length=512, primary_key=True)
    abilities = models.JSONField()
    artist = models.CharField(max_length=512, default=None, null=True)
    ancientTrait = models.JSONField(default=None, null=True)
    attacks = models.JSONField(default=None, null=True)
    convertedRetreatCost = models.SmallIntegerField(default=None, null=True)
    evolvesFrom = models.CharField(max_length=512, default=None, null=True)
    flavorText = models.TextField(default=None, null=True)
    hp = models.SmallIntegerField(default=None, null=True)
    images = models.JSONField(default=None, null=True)
    legalities = models.JSONField(default=None, null=True)
    regulationMark = models.CharField(max_length=5, default=None, null=True)
    name = models.CharField(max_length=512)
    nationalPokedexNumbers = models.JSONField(default=None, null=True)
    number = models.CharField(max_length=16, default=None, null=True)
    rarity = models.CharField(max_length=512, default=None, null=True)
    resistances = models.JSONField(default=None, null=True)
    retreatCost = models.JSONField(default=None, null=True)
    rules = models.JSONField(default=None, null=True)
    sets = models.JSONField(default=None, null=True)
    subtypes = models.JSONField(default=None, null=True)
    supertype = models.JSONField(default=None, null=True)
    tcgplayer = models.JSONField(default=None, null=True)
    types = models.JSONField(default=None, null=True)
    weaknesses = models.JSONField(default=None, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name:
            return self.name + " | " + self.id
        else:
            return "None"
        
    class meta:
        ordering = ['sets.name']
