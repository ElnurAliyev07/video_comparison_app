from django.urls import path
from .import views

urlpatterns = [
    path('', views.choose_videos, name='choose_videos'),
]
