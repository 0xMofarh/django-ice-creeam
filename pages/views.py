from django.shortcuts import render
from django.http import HttpResponse
from .models import Work, Info,Carousel
# Create your views here.


def index(request):
    post = Work.objects.all().filter(active=True)
    info = Info.objects.all()
    Carousels = Carousel.objects.all()
    return render(request, 'pages\index.html', {'data': post, 'info': info, 'Carousel': Carousels})


def about(request):
    return render(request, 'pages\\about.html')
    pass

def contact(request):
    return render(request, 'pages\contact.html')
    pass