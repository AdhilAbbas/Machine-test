from rest_framework import serializers
from .models import Upload

class UploadSerializer(serializers.ModelSerializer):

    picture = serializers.ImageField(required=False)

    class Meta:
        model = Upload
        fields = [ 'picture']


