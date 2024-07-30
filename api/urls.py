# api/urls.py
from django.urls import path
from . import views

urlpatterns = [
     path('books',views.manageBooks,name='books'),
]
