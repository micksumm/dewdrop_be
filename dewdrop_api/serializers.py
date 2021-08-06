from django.contrib.auth.models import User
from rest_framework import serializers
from dewdrop.models import Condition, Product, ProductConditionSolution

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'ingredients', 'description', 'link' )

class ConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condition
        fields = ('__all__')


class ProductConditionSolutionSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)
    conditions = ConditionSerializer(many=True, read_only=True)

    class Meta:
        model = ProductConditionSolution
        fields = ('conditions', 'products')


