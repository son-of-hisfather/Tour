from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
CATEGORY_CHOICES = (
    # ('Tropical', 'Tropical'),
    # ('Mountain', 'Alpine'),
    ('Urban', 'Cityscapes'),
    ('Historical', 'Heritage'),
    ('Coastal', 'Seaside'),
)


    # def __str__(self):
    #     return self.name

#Destination model
class Destination(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='destinations/')
    description = models.TextField(blank= True, null= True)
    tours_available = models.TextField()
    starting_price = models.IntegerField(default=0)
    tags = TaggableManager()
    location_map = models.URLField(help_text="Google Maps URL", blank=True)
    category = models.CharField(max_length=300, choices=CATEGORY_CHOICES, default='Coastal')
    country = models.CharField(max_length=100, default="") 
     
    
    def __str__(self):
        return self.name
    
#Must visit attraction model
class Attraction(models.Model):
    tour = models.ForeignKey(Destination, related_name='attractions', on_delete=models.CASCADE,)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='attractions/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.tour.name}"
    
#Available tours model
class Experience(models.Model):
    tour = models.ForeignKey(Destination, related_name='experiences', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='experiences/')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    time = models.CharField(max_length=100, blank=True, null=True)
    tour_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)

    def __str__(self):
        return f"{self.title} - {self.tour.name}"
    
#About model
class About(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='about/')
    countries_count = models.PositiveIntegerField(default=0)
    travelers_count = models.IntegerField(default=0)
    story_badge = models.CharField(max_length=100, default='Our Story')
    story_title = models.CharField(max_length=255)
    story_text = models.TextField(blank=True, null=True)
    vision_badge = models.CharField(max_length=100, default='Our Vision')
    vision_title = models.CharField(max_length=255)
    vision_text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
    
#Newsletter model
class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    subscribed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
class Contact(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255)
    email_name = models.CharField(max_length=100, blank=True, null=True)
    email_primary = models.EmailField()
    email_secondary = models.EmailField(blank=True, null=True)
    hours_name = models.CharField(max_length=100, blank=True, null=True)
    hours = models.CharField(max_length=255)
    maps_embed = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name 


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"



