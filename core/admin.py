from django.contrib import admin
from .models import Facility, ComponentInfo, Device, UserProfile

# Admin configuration for Facility model
@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    """
    Admin interface for managing e-waste recycling facilities
    """
    list_display = ['name', 'city', 'pincode', 'contact', 'created_at']
    list_filter = ['city', 'created_at']
    search_fields = ['name', 'city', 'pincode', 'address']
    ordering = ['city', 'name']
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'contact')
        }),
        ('Location Details', {
            'fields': ('address', 'city', 'pincode', 'latitude', 'longitude')
        }),
        ('Accepted Items', {
            'fields': ('accepted_items',)
        }),
    )


# Admin configuration for ComponentInfo model
@admin.register(ComponentInfo)
class ComponentInfoAdmin(admin.ModelAdmin):
    """
    Admin interface for managing harmful component information
    """
    list_display = ['component', 'icon', 'created_at']
    search_fields = ['component', 'found_in']
    ordering = ['component']
    fieldsets = (
        ('Component Details', {
            'fields': ('component', 'icon', 'found_in')
        }),
        ('Impact Information', {
            'fields': ('health_effect', 'environmental_effect')
        }),
    )


# Admin configuration for Device model
@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    """
    Admin interface for managing electronic devices and their metal content
    """
    list_display = ['brand', 'model_name', 'device_type', 'estimated_value', 'get_point_value', 'created_at']
    list_filter = ['device_type', 'brand', 'created_at']
    search_fields = ['brand', 'model_name']
    ordering = ['brand', 'model_name']
    fieldsets = (
        ('Device Information', {
            'fields': ('brand', 'model_name', 'device_type')
        }),
        ('Metal Content (mg)', {
            'fields': ('gold_mg', 'silver_mg', 'copper_mg')
        }),
        ('Value', {
            'fields': ('estimated_value',)
        }),
    )

    def get_point_value(self, obj):
        """Display point value in admin list"""
        return obj.get_point_value()
    get_point_value.short_description = 'Points'


# Admin configuration for UserProfile model
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    """
    Admin interface for managing user profiles and recycling statistics
    """
    list_display = ['user', 'points', 'total_recycled', 'co2_saved', 'get_rank', 'created_at']
    list_filter = ['created_at']
    search_fields = ['user__username', 'user__email']
    ordering = ['-points']
    readonly_fields = ['created_at', 'updated_at']
    fieldsets = (
        ('User', {
            'fields': ('user',)
        }),
        ('Statistics', {
            'fields': ('points', 'total_recycled', 'co2_saved')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def get_rank(self, obj):
        """Display user rank in admin list"""
        return obj.get_rank()
    get_rank.short_description = 'Rank'
