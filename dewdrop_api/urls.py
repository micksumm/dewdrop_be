from django.urls import path
# from .views import PostList, PostDetail
#PostList and PostDetail are the names of the endpoints

app_name = 'dewdrop_api'

urlpatterns = [ 
    # path('<int:pk>/', PostDetail.as_view(), name='detailcreate'), #this will show individual post
    # path('', PostList.as_view(), name='listcreate'), #this will show all the posts
]