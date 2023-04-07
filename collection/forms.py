from django import forms
from .models import CollectionItem

import datetime

class CollectionItemForm(forms.Form):
    card = forms.CharField(widget=forms.HiddenInput())
    quantity = forms.IntegerField(widget=forms.NumberInput(attrs={"value":0}))

    