# serializers.py
from rest_framework import serializers
from .models import CleanersInfo

class CleanersInfoSerializer(serializers.ModelSerializer):
    # TODO: override is_valid method

    # def set_id(self):
    #     self.validated_data['id'] = CleanersInfo.objects.latest('id').id + 1;

    class Meta:
        model = CleanersInfo
        fields = '__all__'