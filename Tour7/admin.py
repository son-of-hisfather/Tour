from django.contrib import admin
from .models import Destination

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
    






