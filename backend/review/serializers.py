from rest_framework import serializers
from .models import method_reivew

class methodReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model=method_reivew
        fields="__all__"

        
    
    