from django.contrib import admin
from .models import Feedback

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    """
    Admin interface for Feedback model
    Allows viewing and analyzing user feedback
    """
    list_display = ['name', 'email', 'rating', 'get_rating_stars', 'created_at', 'user']
    list_filter = ['rating', 'created_at']
    search_fields = ['name', 'email', 'comments']
    readonly_fields = ['created_at', 'updated_at']
    ordering = ['-created_at']
    
    fieldsets = (
        ('User Information', {
            'fields': ('user', 'name', 'email')
        }),
        ('Feedback Details', {
            'fields': ('rating', 'comments')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    def get_rating_stars(self, obj):
        return obj.get_rating_display_text()
    get_rating_stars.short_description = 'Rating Stars'
