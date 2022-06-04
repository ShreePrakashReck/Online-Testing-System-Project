from django.urls import path
from .views import *
urlpatterns = [
    path('',greeting),
    path('about/',about),
    path('contacts/',contacts),
    path('hello/',greeting),
]
