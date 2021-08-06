from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dewdrop.urls', namespace='dewdrop')),
    path('api/', include('dewdrop_api.urls', namespace='dewdrop_api')),
]
