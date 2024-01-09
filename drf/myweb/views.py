from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view


# Function Based View
@api_view(['GET'])
def helloAPI(req) :
    return Response("SIUUUU")


# Class Based View
class HelloAPI(APIView):
    def get(self, req) :
        return Response("Class Based View SIUUUU")