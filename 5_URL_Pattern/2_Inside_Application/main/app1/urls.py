from . import views
from django.urls import path

urlpatterns = [
    path('', views.viwe1, name='view1'),
]