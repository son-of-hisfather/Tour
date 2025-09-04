from django.contrib import admin
from .models import Destination, Attraction, Experience, About, Newsletter, Contact, ContactMessage, Booking, HomeAbout

class DestinationAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'title', 'starting_price', 'description',
        'tours_available', 'location_map', 'image', 'category', 'display_tags'
    ]
    search_fields = ['name', 'title']
    list_filter = ['category', 'starting_price']

    #required for 'display_tags' to work
    def display_tags(self, obj):
        return ", ".join(tag.name for tag in obj.tags.all())
#custom admin
admin.site.register(Destination, DestinationAdmin)

admin.site.register(Attraction)
list_display = ['tour', 'name', 'image' 'description']
search_fields = ['name', 'tour__name']

admin.site.register(Experience)
list_display = ['tour', 'image', 'title', 'description', 'rating', 'time', 'tour_price']
search_fields = ['title', 'tour__name']

admin.site.register(About)
list_display = ['title', 'description', 'image', 'country_count', 'travelers_count', 'story_badge', 'story_title', 'story_text', 'vision_badge', 'vision_title', 'vision_text']
search_fields = ['title']

admin.site.register(Newsletter)
list_display = ['email', 'subscribed_at']
search_fields = ['email']

admin.site.register(Contact)
list_display = ['name', 'address', 'email_name', 'email_primary', 'email_secondary', 'hours', 'maps_embed']
search_fields = ['name', 'email_primary', 'email_secondary']

admin.site.register(ContactMessage)
list_display = ['name', 'email', 'subject', 'sent_at']
search_fields = ['name', 'email', 'subject']

admin.site.register(Booking)
list_display = ['destination', 'check_in_date', 'check_out_date', 'adults', 'children', 'tour_type', 'created_at']  
search_fields = ['destination__name', 'tour_type']

admin.site.register(HomeAbout)
list_display = ['title', 'description', 'travelers', 'countries', 'years', 'image', 'badge_number', 'badge_text']
search_fields = ['title'] 






