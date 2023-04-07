from django.urls import path
from . import views

app_name='collection'

urlpatterns=[
    path('ajax/addCard',views.ajaxAddCardView,name='ajaxAdd'),
    path('view',views.CollectionView, name="CollectionView")
]