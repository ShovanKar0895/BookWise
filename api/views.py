from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from api.models import BookModel

@api_view(['GET'])
def fetchBooks(request):

    books_list = BookModel.objects.filter(title='The Odyssey')
    return JsonResponse(books_list[0].author,safe=False)