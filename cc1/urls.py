from django.urls import path
from cc1.views import *
app_name='any'
urlpatterns=[
    path('cc/',cc,name='cc'),
]