from django.urls import path
from . import views

app_name='pages'

urlpatterns=[
    path('', views.Index, name="index"),
    path('results/', views.Results, name='results'),
]