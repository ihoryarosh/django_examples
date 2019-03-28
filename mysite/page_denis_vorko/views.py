from django.shortcuts import render
from .models import Job

# Create your views here.
def index(request):
    jobs = Job.objects.all()
    return render(request, 'page_denis_vorko/index.html', context={'jobs':jobs})