from django.urls import path
from . import views

app_name='cards'

urlpatterns=[
    path('<str:card_id>',views.CardView,name='CardView') 
]