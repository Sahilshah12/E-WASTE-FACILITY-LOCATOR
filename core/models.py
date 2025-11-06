from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Model for E-Waste Recycling Facilities
class Facility(models.Model):
    """
    Represents an e-waste recycling facility
    Contains location, contact details, and accepted items
    """
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    contact = models.CharField(max_length=15)
    accepted_items = models.TextField(help_text="Comma-separated list of accepted e-waste items")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Facilities"
        ordering = ['city', 'name']

    def __str__(self):
        return f"{self.name} - {self.city}"


# Model for Harmful Component Information
class ComponentInfo(models.Model):
    """
    Educational information about harmful components in e-waste
    Used for awareness and learning modules
    """
    component = models.CharField(max_length=100, unique=True)
    found_in = models.TextField(help_text="Devices where this component is typically found")
    health_effect = models.TextField(help_text="Impact on human health")
    environmental_effect = models.TextField(help_text="Impact on environment")
    icon = models.CharField(max_length=50, default="⚠️", help_text="Emoji or icon representation")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Component Information"
        ordering = ['component']

    def __str__(self):
        return self.component


# Model for Electronic Devices
class Device(models.Model):
    """
    Represents electronic devices with their metal content and estimated value
    Used for value estimation feature
    """
    DEVICE_TYPES = [
        ('laptop', 'Laptop'),
        ('smartphone', 'Smartphone'),
        ('tablet', 'Tablet'),
        ('desktop', 'Desktop Computer'),
        ('monitor', 'Monitor'),
        ('keyboard', 'Keyboard'),
        ('mouse', 'Mouse'),
        ('printer', 'Printer'),
        ('other', 'Other'),
    ]

    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=200)
    device_type = models.CharField(max_length=20, choices=DEVICE_TYPES, default='other')
    gold_mg = models.DecimalField(max_digits=10, decimal_places=2, help_text="Gold content in milligrams")
    copper_mg = models.DecimalField(max_digits=10, decimal_places=2, help_text="Copper content in milligrams")
    silver_mg = models.DecimalField(max_digits=10, decimal_places=2, help_text="Silver content in milligrams")
    estimated_value = models.DecimalField(max_digits=10, decimal_places=2, help_text="Estimated recovery value in INR")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['brand', 'model_name']
        unique_together = ['brand', 'model_name']

    def __str__(self):
        return f"{self.brand} {self.model_name}"

    def get_point_value(self):
        """Calculate points awarded for recycling this device"""
        return int(self.estimated_value / 10)


# Model for User Profile with Gamification
class UserProfile(models.Model):
    """
    Extended user profile for tracking recycling activity
    Includes gamification elements like points and statistics
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    points = models.IntegerField(default=0, help_text="Points earned from recycling")
    total_recycled = models.IntegerField(default=0, help_text="Total number of devices recycled")
    co2_saved = models.DecimalField(max_digits=10, decimal_places=2, default=0, help_text="CO2 saved in kg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

    def add_recycled_device(self, device):
        """
        Add a recycled device to user's profile
        Updates points, count, and CO2 savings
        """
        from decimal import Decimal
        
        points_earned = device.get_point_value()
        self.points += points_earned
        self.total_recycled += 1
        # Formula: 1 point = 0.05 kg CO2 saved
        # Convert to Decimal to match field type
        self.co2_saved += Decimal(str(points_earned * 0.05))
        self.save()

    def get_rank(self):
        """Get user's rank based on points (1 = highest)"""
        higher_ranked = UserProfile.objects.filter(points__gt=self.points).count()
        return higher_ranked + 1

    class Meta:
        ordering = ['-points']


# Signal to automatically create UserProfile when User is created
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """Automatically create a UserProfile when a new User is created"""
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """Save the UserProfile when User is saved"""
    if hasattr(instance, 'profile'):
        instance.profile.save()
