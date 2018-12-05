from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.viewallblogs, name='blog'),
    path('<str:id_slug>', views.post, name='blogpost')
]