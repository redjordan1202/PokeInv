from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

class Collection(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return ("%s's Collection" % self.user.username)

class CollectionItem(models.Model):
    card = models.ForeignKey('cards.Card', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return ("%s | %i | %s" % (self.card, self.quantity, self.collection))
