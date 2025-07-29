from django.shortcuts import render
from .models import Destination

# Create your views here.

def home(request):
    return render(request, 'tour/index.html')


def about(request):
    return render(request, 'tour/about.html')

def destinations(request):
    destinations = Destination.objects.all()  # fetch all destination objects
    return render(request, 'tour/destinations.html', {'destinations': destinations})

def contact(request):
    return render(request, 'tour/contact.html')

def tours(request):
    return render(request, 'tour/tours.html')

def gallery(request):
    return render(request, 'tour/gallery.html')

def destination_details(request):
    return render(request, 'tour/destination-details.html')

# def category_list(request):
#     categories = Category.objects.all()  # fetch all category objects
#     return render(request, 'tour/category_list.html', {'categories': categories})

    