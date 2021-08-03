from rest_framework import serializers
from dewdrop.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'ingredients', 'description', 'link' )