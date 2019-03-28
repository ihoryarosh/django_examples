from django.shortcuts import render

# Create your views here.
def index(request):
    number = [i for i in range(27)]
    return render(request, 'page_denis_vorko/index.html', context={'numbers':number})