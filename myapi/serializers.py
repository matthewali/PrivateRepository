#serializers.py
from rest_framework import serializers
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from django.db.models.aggregates import Avg, Count
from django.db.models.expressions import OrderBy
from rest_framework import serializers


class BookSerializer (serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BookDetails
        fields = ('ID', 'Price', 'CopiesSold')


class authorserializer (serializers.ModelSerializer):
    def create (self, validated_data):
    	return Author.objects.create(**validated_data)
    
    class Meta:
        model = Author
        fields = [
            "AuthorID",
            "FName",
            "LName",
            "Biography",
        ]


