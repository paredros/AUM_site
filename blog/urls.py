from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.bloggeneral, name='blog'),
    path('<str:id_slug>', views.postenhanced, name='blogpost'),
    path('view/all', views.viewallforce, name='blogall')
]