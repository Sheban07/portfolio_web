
from django.shortcuts import render, redirect
from .forms import ContactForm



# Create your views here.
def home(request):
    return render(request, 'web/home.html')

def about(request):
    return render(request, 'web/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'web/contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'web/contact.html', {'form': form})