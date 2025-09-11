from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Destination, Attraction, Experience, About, Newsletter, Contact, ContactMessage, Booking, HomeAbout, Customer

# Create your views here.
def home(request):
    if request.method == 'POST':
        destination_id = request.POST.get("destination")
        check_in = request.POST.get("check_in_date")
        check_out = request.POST.get("check_out_date")
        adults = request.POST.get("adults")
        children = request.POST.get("children")
        tour_type = request.POST.get("tour_type")

        destination = Destination.objects.get(id=destination_id)

        Booking.objects.create(
            destination=destination,
            check_in_date=check_in,
            check_out_date=check_out,
            adults=adults,
            children=children,
            tour_type=tour_type
        )
        messages.success(request, 'Booking has been successfully created!')
        return redirect('home')

    # fetch destinations (remove slicing so all show up)
    destinations = Destination.objects.all()
    home_about = HomeAbout.objects.first()
    customers = Customer.objects.all()

    context = {
        "destinations": destinations,
        "home_about": home_about,
        "customers": customers,
    }
    return render(request, 'tour/index.html', context)



def about(request):
    about = About.objects.all()  

    return render(request, 'tour/about.html', {'about': about})

def destinations(request):
    destinations = Destination.objects.all()  # fetch all destination objects
    return render(request, 'tour/destinations.html', {'destinations': destinations})

def contact(request):
    contacts = Contact.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')

        # Validation
        if not name or not email or not subject or not message_text:
            messages.error(request, 'All fields are required.')
            return redirect('contact')

        # Save message
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )

        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'tour/contact.html', {'contacts': contacts})

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

def subscriber(request):
    if request.method == 'POST':
        email = request.POST.get('email')

        if not email:
            messages.error(request, 'Email is required.')
            return redirect('about')
        
        # Validate email input
        if not email or '@' not in email or '.' not in email.split('@')[-1]:
            messages.error(request, 'Please enter a valid email address.')
            return redirect('about')
        
        # Check if the email is already subscribed
        #check if email already exists
        if Newsletter.objects.filter(email=email).exists():
            messages.warning(request, 'This email is already subscribed.')
            return redirect('about')
        
        # Save the email to the Newsletter model
         # Save the email to the database
        Newsletter.objects.create(email=email)
        messages.success(request, 'You have successfully subscribed to our newsletter!')
        return redirect('about')
    else:
        messages.error(request, 'Subscription failed. Please try again.')
        return redirect('about')