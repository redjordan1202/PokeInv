from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class CollectionItem(models.Model):
    card = models.ForeignKey('cards.Card', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)
