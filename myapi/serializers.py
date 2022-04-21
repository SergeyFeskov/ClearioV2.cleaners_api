# serializers.py
from rest_framework import serializers
from .models import CleanersInfo

class CleanersInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CleanersInfo
        fields = ('id', 'name', 'surname', 'city', 'phonenumber', 'isworking', 'rating')