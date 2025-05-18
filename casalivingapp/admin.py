from django.contrib import admin
from import_export.admin import ExportMixin
from .models import (
    House, Room, RoomImage, GalleryImage, ContactForm, TeamMember,
    AmenityTag, HouseAmenity, HouseImage, Review
)

# House Admin
class HouseAmenityInline(admin.TabularInline):
    model = HouseAmenity
    extra = 1

# Inline for Rooms inside HouseAdmin
class RoomInline(admin.TabularInline):
    model = Room
    extra = 1

# House Admin
class HouseImageInline(admin.TabularInline):
    model = HouseImage
    extra = 1

class HouseAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'created_at')
    search_fields = ('title', 'location')
    ordering = ('-created_at',)
    inlines = [HouseImageInline,RoomInline]


# Room Admin
class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1





class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'house', 'created_at')
    search_fields = ('name', 'house__title')
    list_filter = ('house',)
    ordering = ('-created_at',)
    inlines = [RoomImageInline]
    filter_horizontal = ('amenities',)  # For selecting room amenities in admin


# RoomImage Admin
class RoomImageAdmin(admin.ModelAdmin):
    list_display = ('room', 'uploaded_at')
    list_filter = ('room',)
    ordering = ('-uploaded_at',)

# RoomImage Admin
class HouseImageAdmin(admin.ModelAdmin):
    list_display = ('house', 'uploaded_at')
    list_filter = ('house',)
    ordering = ('-uploaded_at',)



# Gallery Image Admin
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'uploaded_at')
    ordering = ('-uploaded_at',)


# Contact Form Admin
class ContactFormAdmin(ExportMixin, admin.ModelAdmin):
    list_display = ('full_name', 'email', 'contact_number', 'room', 'submitted_at')
    search_fields = ('full_name', 'email', 'contact_number')
    list_filter = ('room',)
    ordering = ('-submitted_at',)


# Team Member Admin
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'created_at')
    search_fields = ('name', 'role')
    ordering = ('-created_at',)


# Amenity Tag Admin
class AmenityTagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


# House Amenity Admin (optional direct management, not required if using inline)
class HouseAmenityAdmin(admin.ModelAdmin):
    list_display = ('house', 'tag')
    list_filter = ('house', 'tag')
    search_fields = ('house__title', 'tag__name')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer_name', 'reviewer_location', 'rating', 'created_at')
    list_filter = ('rating', 'created_at', 'reviewer_location')
    search_fields = ('reviewer_name', 'reviewer_location', 'description')
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)

# Register all models
admin.site.register(House, HouseAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomImage, RoomImageAdmin)
admin.site.register(HouseImage, HouseImageAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(AmenityTag, AmenityTagAdmin)
admin.site.register(HouseAmenity, HouseAmenityAdmin)
admin.site.register(Review, ReviewAdmin)


