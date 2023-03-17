from django.db import models


# Create your models here.


class Card_Set(models.Model):
    id = models.CharField(max_length=512, primary_key=True)
    images = models.JSONField(default=None, null=True)
    legalities = models.JSONField(default=None, null=True)
    name = models.CharField(max_length=512)
    printedTotal = models.SmallIntegerField(default=None, null=True)
    ptcgoCode = models.CharField(max_length=512, default=None, null=True)
    releaseDate = models.DateField(default=None, null=True, auto_now=False)
    series = models.CharField(max_length=512, default=None, null=True)
    total = models.SmallIntegerField(default=None, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.name:
            return self.name
        else:
            return "None"
