from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from pybo.models import Question
from pybo.serializers import QuestionSerializer


# Function Based View
@api_view(['GET'])
def helloAPI(req) :
    return Response("SIUUUU")


# Class Based View
class HelloAPI(APIView) :
    def get(self, req) :
        return Response("Class Based View SIUUUU")
    

@api_view(['GET', 'POST'])
def questionsAPI(req) :
    if req.method == 'GET' :
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif req.method == 'POST' :
        serializer = QuestionSerializer(data=req.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def questionAPI(req, id) :
    question = Question.objects.get(pk=id)
    serializer = QuestionSerializer(question)
    return Response(serializer.data, status=status.HTTP_200_OK)