from rest_framework import serializers
from .models import Sentence

class SentenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sentence
        fields = ['id', 'content', 'author', 'created_at', 'updated_at']