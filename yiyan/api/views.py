from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Sentence
from .serializers import SentenceSerializer
import random

class SentenceViewSet(viewsets.ModelViewSet):
    queryset = Sentence.objects.all()
    serializer_class = SentenceSerializer

@api_view(['GET'])
def random_sentence(request):
    count = Sentence.objects.count()
    if count == 0:
        return Response({'error': 'No sentences found'}, status=status.HTTP_404_NOT_FOUND)
    
    random_index = random.randint(0, count - 1)
    sentence = Sentence.objects.all()[random_index]
    serializer = SentenceSerializer(sentence)
    return Response(serializer.data)

@api_view(['POST'])
def create_sentence(request):
    serializer = SentenceSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_sentence(request, pk):
    sentence = get_object_or_404(Sentence, pk=pk)
    serializer = SentenceSerializer(sentence, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_sentence(request, pk):
    sentence = get_object_or_404(Sentence, pk=pk)
    sentence.delete()
    return Response(status=status.HTTP_204_NO_CONTENT) 