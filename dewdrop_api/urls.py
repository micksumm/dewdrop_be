from django.urls import path
from .views import ProductList, ConditionList,  ProductConditionSolutionList, ProductDetail, ConditionDetail
#PostList and PostDetail are the names of the endpoints

app_name = 'dewdrop_api'

urlpatterns = [ 
    path('products/<int:pk>/', ProductDetail.as_view(), name='detailcreate'), #this will show individual post
    path('products/', ProductList.as_view(), name='listcreate'), #this will show all the posts
    path('conditions/', ConditionList.as_view(), name='listcreate'),
    path('conditions/<int:pk>/', ConditionDetail.as_view(), name='detailcreate'),
    path('solutions/', ProductConditionSolutionList.as_view(), name='list')
]