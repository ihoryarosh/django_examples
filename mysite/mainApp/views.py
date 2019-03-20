from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'mainApp/home_page.html')


def contact(request):
    diction = {'values': ['If You have any question, call me please :',
                                                   '0980788998', 'example@mail.ru']}
    return render(request, 'mainApp/basic.html', diction)

