from rest_framework import generics, request
from dewdrop.models import Condition, Product # ProductConditionSolution
from .serializers import ProductSerializer, ConditionSerializer #ProductConditionSolutionSerializer

class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pass

class ProductDetail(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pass

class ConditionList(generics.ListCreateAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    pass

class ConditionDetail(generics.RetrieveDestroyAPIView):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    pass

# class ProductConditionSolutionList(generics.ListAPIView):
#     queryset = ProductConditionSolution.objects.all()
#     serializer_class = ProductConditionSolutionSerializer
#     pass

# class ProductCondition(request):
#     product = Product.objects.get(id=2)
#     cond = Condition.objects.get(id=3)

#     product.conditions.add(cond)
#     product.save()

# another view
# class ProductDetail(generics.blahblah):
    # product = Product.objects.get(id=user_id)
    # product_json = {
    #     'name': product.name,
    #     'conditions': []
    # }
    # for condition in product.conditions.all():
    #     product_json['conditions'].append(condition)
