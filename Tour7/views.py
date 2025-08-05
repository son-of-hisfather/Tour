from django.shortcuts import render, get_object_or_404
from .models import Destination, Attraction, Experience

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

def destination_details(request, pk):
    destination = get_object_or_404(Destination, pk=pk)
    attraction = Attraction.objects.filter(tour=destination)
    experience = Experience.objects.filter(tour=destination)
    return render(request, 'tour/destination-details.html', {
        'destination': destination,
        'attractions': attraction,
        'experiences': experience
    })

# def category_list(request):
#     categories = Category.objects.all()  # fetch all category objects
#     return render(request, 'tour/category_list.html', {'categories': categories})

    