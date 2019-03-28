from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_MA'),
    path('contact/', views.contact, name='contact'),
]