from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from .models import Facility, ComponentInfo, Device, UserProfile
from .forms import DeviceSearchForm, FacilitySearchForm, UserRegistrationForm, RecycleDeviceForm
import random


# Home Page View
def home(request):
    """
    Landing page with overview and call-to-action buttons
    Shows statistics and featured information
    """
    context = {
        'total_facilities': Facility.objects.count(),
        'total_devices': Device.objects.count(),
        'total_users': UserProfile.objects.count(),
    }
    return render(request, 'core/home.html', context)


# Facility Locator View
def facility_locator(request):
    """
    Display e-waste facilities on an interactive map
    Supports filtering by city or pincode
    """
    form = FacilitySearchForm(request.GET or None)
    facilities = Facility.objects.all()
    
    # Apply search filters
    if form.is_valid():
        search_type = form.cleaned_data.get('search_type')
        search_query = form.cleaned_data.get('search_query')
        
        if search_type == 'city' and search_query:
            facilities = facilities.filter(city__icontains=search_query)
        elif search_type == 'pincode' and search_query:
            facilities = facilities.filter(pincode__icontains=search_query)
    
    context = {
        'form': form,
        'facilities': facilities,
    }
    return render(request, 'core/locator.html', context)


# Educational Pop-ups View
def learn(request):
    """
    Display random harmful component information
    Educational feature about e-waste dangers
    """
    components = ComponentInfo.objects.all()
    
    if components.exists():
        # Get a random component or the one requested
        component_id = request.GET.get('id')
        if component_id:
            component = get_object_or_404(ComponentInfo, id=component_id)
        else:
            component = random.choice(components)
    else:
        component = None
    
    context = {
        'component': component,
        'total_components': components.count(),
    }
    return render(request, 'core/learn.html', context)


# Device Value Estimator View
def estimate(request):
    """
    Estimate device value based on brand and model
    Shows metal content and potential earnings
    """
    form = DeviceSearchForm(request.POST or None)
    device = None
    not_found = False
    
    if request.method == 'POST' and form.is_valid():
        brand = form.cleaned_data['brand']
        model_name = form.cleaned_data['model_name']
        
        # Search for device (case-insensitive)
        try:
            device = Device.objects.get(
                brand__iexact=brand,
                model_name__icontains=model_name
            )
        except Device.DoesNotExist:
            not_found = True
            messages.warning(request, f"Device '{brand} {model_name}' not found in our database.")
        except Device.MultipleObjectsReturned:
            # If multiple matches, get the first one
            device = Device.objects.filter(
                brand__iexact=brand,
                model_name__icontains=model_name
            ).first()
    
    context = {
        'form': form,
        'device': device,
        'not_found': not_found,
    }
    return render(request, 'core/estimate.html', context)


# User Dashboard View
@login_required
def dashboard(request):
    """
    User dashboard showing recycling statistics and gamification
    Displays points, recycled devices, CO2 saved, and rank
    """
    # Get or create profile for users who don't have one
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    recycle_form = RecycleDeviceForm(request.POST or None)
    
    # Handle device recycling submission
    if request.method == 'POST' and recycle_form.is_valid():
        device = recycle_form.cleaned_data['device']
        profile.add_recycled_device(device)
        messages.success(
            request,
            f"Congratulations! You've recycled a {device}. Earned {device.get_point_value()} points!"
        )
        return redirect('core:dashboard')
    
    # Get leaderboard (top 5 users)
    leaderboard = UserProfile.objects.all()[:5]
    
    context = {
        'profile': profile,
        'recycle_form': recycle_form,
        'leaderboard': leaderboard,
        'user_rank': profile.get_rank(),
    }
    return render(request, 'core/dashboard.html', context)


# User Registration View
def register(request):
    """
    User registration page
    Creates new user account with profile
    """
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    form = UserRegistrationForm(request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, f"Welcome {user.username}! Your account has been created successfully.")
        return redirect('core:dashboard')
    
    context = {'form': form}
    return render(request, 'core/register.html', context)


# User Login View
def user_login(request):
    """
    User login page
    Authenticates existing users
    """
    if request.user.is_authenticated:
        return redirect('core:dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            next_url = request.GET.get('next', 'core:dashboard')
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'core/login.html')


# User Logout View
def user_logout(request):
    """
    Logout user and redirect to home
    """
    logout(request)
    messages.info(request, "You've been logged out successfully.")
    return redirect('core:home')


# API endpoint for facilities (AJAX/JSON)
def facilities_json(request):
    """
    Return facilities as JSON for map markers
    Used by Leaflet.js in the frontend
    """
    facilities = Facility.objects.all()
    
    # Apply filters if provided
    city = request.GET.get('city')
    pincode = request.GET.get('pincode')
    
    if city:
        facilities = facilities.filter(city__icontains=city)
    if pincode:
        facilities = facilities.filter(pincode__icontains=pincode)
    
    # Format data for JSON response
    data = [{
        'id': f.id,
        'name': f.name,
        'address': f.address,
        'city': f.city,
        'pincode': f.pincode,
        'latitude': float(f.latitude),
        'longitude': float(f.longitude),
        'contact': f.contact,
        'accepted_items': f.accepted_items,
    } for f in facilities]
    
    return JsonResponse(data, safe=False)
