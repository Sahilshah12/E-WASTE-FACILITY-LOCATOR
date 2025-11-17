from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Avg, Count
from .forms import UserRegistrationForm, UserLoginForm, FeedbackForm
from .models import Feedback

def home(request):
    
    total_feedbacks = Feedback.objects.count()
    avg_rating = Feedback.objects.aggregate(Avg('rating'))['rating__avg'] or 0
    recent_feedbacks = Feedback.objects.all()[:5]
    
    context = {
        'total_feedbacks': total_feedbacks,
        'avg_rating': round(avg_rating, 1),
        'recent_feedbacks': recent_feedbacks,
    }
    return render(request, 'RPL/home.html', context)

def register_view(request):
    
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('RPL:home')
    
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome {user.username}! Your account has been created successfully.')
            
            request.session.set_expiry(1209600) 
            return redirect('RPL:home')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserRegistrationForm()
    
    return render(request, 'RPL/register.html', {'form': form})

def login_view(request):
   
    if request.user.is_authenticated:
        messages.info(request, 'You are already logged in.')
        return redirect('RPL:home')
    
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {user.username}!')
                
                remember_me = request.POST.get('remember_me')
                if remember_me:
                    request.session.set_expiry(1209600) 
                else:
                    request.session.set_expiry(0) 
                

                next_url = request.GET.get('next', 'RPL:home')
                return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    
    return render(request, 'RPL/login.html', {'form': form})

@login_required(login_url='RPL:login')
def logout_view(request):
    
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('RPL:home')

@login_required(login_url='RPL:login')
def feedback_view(request):
    """
    Feedback form for logged-in users
    Validates and stores feedback in database
    """
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            
            messages.success(request, 'Thank you for your feedback! We appreciate your input.')
            return redirect('RPL:feedback_success')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        
        initial_data = {
            'name': f"{request.user.first_name} {request.user.last_name}".strip() or request.user.username,
            'email': request.user.email
        }
        form = FeedbackForm(initial=initial_data)
    
    return render(request, 'RPL/feedback.html', {'form': form})

def feedback_success(request):
   
    return render(request, 'RPL/feedback_success.html')

@login_required(login_url='RPL:login')
def feedback_list(request):
   
    if not request.user.is_staff:
        messages.error(request, 'You do not have permission to view this page.')
        return redirect('RPL:home')
    
    feedbacks = Feedback.objects.all()
    
    stats = {
        'total': feedbacks.count(),
        'avg_rating': feedbacks.aggregate(Avg('rating'))['rating__avg'] or 0,
        'rating_distribution': {
            i: feedbacks.filter(rating=i).count() for i in range(1, 6)
        }
    }
    
    context = {
        'feedbacks': feedbacks,
        'stats': stats
    }
    return render(request, 'RPL/feedback_list.html', context)

@login_required(login_url='RPL:login')
def dashboard(request):
    
    user_feedbacks = Feedback.objects.filter(user=request.user)
    
    context = {
        'user_feedbacks': user_feedbacks,
        'total_feedbacks': user_feedbacks.count(),
    }
    return render(request, 'RPL/dashboard.html', context)
