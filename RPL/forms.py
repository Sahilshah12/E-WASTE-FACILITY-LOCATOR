from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Feedback

class UserRegistrationForm(UserCreationForm):
    """
    Extended registration form with email and name fields
    """
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your email'
    }))
    first_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First name'
    }))
    last_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last name'
    }))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirm password'})
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email

class UserLoginForm(AuthenticationForm):
    """
    Custom login form with styled fields
    """
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Password'
    }))

class FeedbackForm(forms.ModelForm):
    """
    Form for users to submit feedback about website features
    Includes validation for all fields
    """
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'rating', 'comments']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'your.email@example.com',
                'required': True
            }),
            'rating': forms.RadioSelect(attrs={
                'class': 'form-check-input'
            }),
            'comments': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your thoughts about our website features...',
                'rows': 5,
                'required': True
            })
        }
    
    def clean_name(self):
        """Validate that name doesn't contain numbers"""
        name = self.cleaned_data.get('name', '')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError("Name should not contain numbers.")
        if len(name.strip()) < 2:
            raise forms.ValidationError("Please enter a valid name (at least 2 characters).")
        return name.strip()
    
    def clean_email(self):
        """Validate email format"""
        email = self.cleaned_data.get('email', '')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email.lower()
    
    def clean_rating(self):
        """Validate rating is within range"""
        rating = self.cleaned_data.get('rating')
        if rating is None:
            raise forms.ValidationError("Please select a rating.")
        if rating < 1 or rating > 5:
            raise forms.ValidationError("Rating must be between 1 and 5.")
        return rating
    
    def clean_comments(self):
        """Validate comments are not empty and have minimum length"""
        comments = self.cleaned_data.get('comments', '')
        if len(comments.strip()) < 10:
            raise forms.ValidationError("Please provide more detailed feedback (at least 10 characters).")
        return comments.strip()