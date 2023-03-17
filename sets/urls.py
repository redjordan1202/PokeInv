from django.urls import path
from . import views

app_name='sets'

urlpatterns=[
    path('all/', views.SetsView, name="SetsView"),
    path('import/', views.ImportSets, name="Import"),
]