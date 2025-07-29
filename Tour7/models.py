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
    
    def __str__(self):
        return self.name
    



