from django.urls import path, include
from django.views.generic import ListView, DetailView
from .models import Article



urlpatterns = [
    path('', ListView.as_view(), name='news/posts.html')
]

# queryset=Article.objects.all().order_by('-date')[:20],
#                              template_name='/news/posts.html')