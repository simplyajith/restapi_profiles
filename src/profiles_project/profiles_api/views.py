from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView

from . import serializers
from rest_framework import status

# Create your views here.

def myView(request):
    ''' Hello world will be printed when myView is called from urls.py'''
    return HttpResponse('Hello World!')

class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self,request,format =None):
        '''Returns a list of API view features'''

        apiview = [
            'Uses http methods as functions',
            'Similar to traditional Django view',
            'Gives you most control over your logic',
            'Is mapped manually to urls'

        ]

        return Response({'message': 'Hello!', 'apiview':apiview})

    def post(self,request):
        '''Create a hello message with our name'''
        serializer = serializers.HelloSerializer(data = request.data)

        if serializer.is_valid():
            name = serializer.data.get('name')
            message ='Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk= None):

        ''' Handles updating a  object'''

        return Response({'message':'put'})

    def patch(self,request,pk= None):

        ''' Handles updating a part of an object'''

        return Response({'message':'patch'})

    def delete(self,request,pk= None):

        ''' Deleting an object'''

        return Response({'message':'Delete'})


