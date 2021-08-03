from django.urls import path
from django.views.generic import TemplateView

app_name = 'dewdrop'

urlpatterns = [
    path('', TemplateView.as_view(template_name="dewdrop/index.html")),
]