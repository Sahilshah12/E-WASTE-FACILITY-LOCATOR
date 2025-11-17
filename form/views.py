from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student

def student_create(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # saves to DB
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'form/student_form.html', {'form': form})

def student_list(request):
    students = Student.objects.all().order_by('name')
    return render(request, 'form/student_list.html', {'students': students})



from django.shortcuts import render, redirect
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # use cleaned data (here we just print or send email)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            # TODO: send email or process the data
            print("Contact form submitted:", name, email, message)
            return redirect('contact_success')  # POST -> redirect -> GET
    else:
        form = ContactForm()

    return render(request, 'form/contact.html', {'form': form})

def contact_success(request):
    return render(request, 'form/contact_success.html')
