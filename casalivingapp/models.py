from django.db import models
from django.core.validators import RegexValidator

# PG House model (e.g., a specific building or apartment)
class House(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.TextField()
    image = models.ImageField(upload_to='houses/')
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
class HouseImage(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='houseImage')
    image = models.ImageField(upload_to='houses/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.house.title}"


# Tags for amenities (e.g., WiFi, AC, Parking, etc.)
class AmenityTag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


# House can have many amenity tags
class HouseAmenity(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='amenities')
    tag = models.ForeignKey(AmenityTag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tag.name} in {self.house.title}"


# Room model linked to House
class Room(models.Model):
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='rooms', null=True, blank=True)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    # The room can select which amenities of its house apply to it
    amenities = models.ManyToManyField(AmenityTag, blank=True, related_name='rooms')

    def __str__(self):
        return f"{self.name} ({self.house.title})" if self.house else self.name


# Each Room can have multiple images
class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='rooms/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.room.name}"


# General Gallery images not linked to Room
class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Gallery Image {self.id}"


# Contact Form linked to Room
class ContactForm(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='inquiries')
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    contact_number = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number.')
        ]
    )
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Query by {self.full_name} for {self.room.name}"


# Your Team Members
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='team/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator

class Review(models.Model):
    reviewer_name = models.CharField(
        max_length=100,
        help_text="Full name of the reviewer"
    )
    
    reviewer_profile_pic = models.ImageField(
        upload_to='reviewers/profile_pics/',
        blank=True,
        null=True,
        help_text="Optional profile picture of the reviewer"
    )
    
    reviewer_location = models.CharField(
        max_length=150,
        blank=True,
        help_text="City or region of the reviewer (optional)"
    )
    
    description = models.TextField(
        max_length=1000,
        help_text="Review content (max 1000 characters)"
    )
    
    rating = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, message="Rating must be at least 1."),
            MaxValueValidator(5, message="Rating must not exceed 5.")
        ],
        help_text="Rating between 1 (worst) and 5 (best)"
    )
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.reviewer_name} ({self.rating}⭐)"

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Review"
        verbose_name_plural = "Reviews"

