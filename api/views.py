from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from api.serializers import BookModelerializer

from api.models import BookModel

@api_view(['GET','POST','PUT','PATCH','DELETE'])
def manageBooks(request):
    
    if request.method == 'GET':
        snippets = BookModel.objects.all().exclude(status='5')[0:2]
        serializer = BookModelerializer(snippets, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookModelerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    elif request.method == 'PUT':
        return Response('PUT Method')
    
    elif request.method == 'PATCH':
        return Response('PATCH Method')
    
    elif request.method == 'DELETE':
        return Response('DELETE Method')
    
    else:
        return Response('None found')
    