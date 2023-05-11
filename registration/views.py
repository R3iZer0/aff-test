from aiohttp import request
from django.urls import path
from django.shortcuts import redirect, render
from .forms import LeadForm
from .models import Lead
from django.http import request



def home(request):
    return render(request, 'home.html', {})


# views.py

from django.shortcuts import render
from .forms import LeadForm

def lead_register(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            # Save the lead to the database
            form.save()
            # Redirect to a "thank you" page or some other page
            return redirect('registration')
    else:
        form = LeadForm()
    return render(request, 'registration.html', {'form': form})

