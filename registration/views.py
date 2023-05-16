from aiohttp import request
from django.urls import path
from django.shortcuts import redirect, render
from .forms import LeadForm
from .models import Lead
from django.http import HttpResponse, request
from django.http import JsonResponse
from openpyxl import Workbook

def home(request):
    return render(request, 'home.html', {})




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



def lead_list(request):
    leads = Lead.objects.all()
    return render(request, 'leads_view.html', {'leads': leads})


def download_table(request):
    leads = Lead.objects.all()  # Replace 'Lead' with your actual model name or queryset
    
    # Create a new workbook and get the active sheet
    workbook = Workbook()
    sheet = workbook.active
    
    # Write the table headers
    headers = ['Id', 'Name', 'Last Name', 'Email', 'Phone', 'Country', 'Experience', 'Registered at']
    for col_num, header in enumerate(headers, 1):
        sheet.cell(row=1, column=col_num, value=header)
    
    # Write the table data
    for row_num, lead in enumerate(leads, 2):
        sheet.cell(row=row_num, column=1, value=lead.id)
        sheet.cell(row=row_num, column=2, value=lead.name)
        sheet.cell(row=row_num, column=3, value=lead.last_name)
        sheet.cell(row=row_num, column=4, value=lead.email)
        sheet.cell(row=row_num, column=5, value=lead.phone)
        sheet.cell(row=row_num, column=6, value=lead.country)
        sheet.cell(row=row_num, column=7, value=lead.experience)
        created_at_naive = lead.created_at.replace(tzinfo=None)
        sheet.cell(row=row_num, column=8, value=created_at_naive)    
    # Create the response object with appropriate headers
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=leads.xlsx'
    
    # Save the workbook to the response object
    workbook.save(response)
    
    return response