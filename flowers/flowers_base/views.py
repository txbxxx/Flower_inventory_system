from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'flowers_base/index.html')


def flower_data(request):
    return None