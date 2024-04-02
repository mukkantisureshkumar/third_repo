from django.urls import path
from bb1.views import *

app_name='any'

urlpatterns=[
    path('bb/',bb,name='bb'),
]
