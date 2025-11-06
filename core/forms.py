from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Device


class DeviceSearchForm(forms.Form):
    """
    Form for searching devices by brand and model
    Used in the Device Value Estimator
    """
    brand = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter device brand (e.g., Apple, Samsung)',
            'autocomplete': 'off'
        })
    )
    model_name = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter model name (e.g., iPhone 12, Galaxy S21)',
            'autocomplete': 'off'
        })
    )

    def clean_brand(self):
        """Normalize brand name"""
        brand = self.cleaned_data.get('brand')
        return brand.strip().title() if brand else ''

    def clean_model_name(self):
        """Normalize model name"""
        model_name = self.cleaned_data.get('model_name')
        return model_name.strip() if model_name else ''


class FacilitySearchForm(forms.Form):
    """
    Form for searching facilities by city or pincode
    Used in the Facility Locator
    """
    SEARCH_CHOICES = [
        ('', 'All Locations'),
        ('city', 'Search by City'),
        ('pincode', 'Search by Pincode'),
    ]
    
    search_type = forms.ChoiceField(
        choices=SEARCH_CHOICES,
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-select',
        })
    )
    
    search_query = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter city name or pincode',
            'autocomplete': 'off'
        })
    )


class UserRegistrationForm(UserCreationForm):
    """
    Extended user registration form with email
    Creates a new user account
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        })
    )
    first_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First name (optional)'
        })
    )
    last_name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last name (optional)'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Choose a username'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add Bootstrap classes to password fields
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirm password'
        })

    def save(self, commit=True):
        """Save the user with email"""
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class RecycleDeviceForm(forms.Form):
    """
    Form for simulating device recycling action
    Used in the dashboard to add recycled devices
    """
    device = forms.ModelChoiceField(
        queryset=Device.objects.all(),
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-select',
        }),
        label='Select Device to Recycle'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the device display in dropdown
        self.fields['device'].label_from_instance = lambda obj: f"{obj.brand} {obj.model_name} (₹{obj.estimated_value})"
