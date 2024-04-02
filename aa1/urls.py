from django.urls import path
from aa1.views import *

app_name='anybody'

urlpatterns=[
    path('aa/',aa,name='aa'),
]
