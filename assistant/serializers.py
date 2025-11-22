from rest_framework import serializers
from .models import products

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = products
        fields = '__all__'
        read_only_fields = ['description']  