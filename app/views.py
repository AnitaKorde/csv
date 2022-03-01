from multiprocessing import Event
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import HttpResponseRedirect

from django.contrib import messages

from django.urls import reverse
import logging
from app.models import Employee
import csv, io

# Create your views here.

def home(request):
    return render(request,template_name='home.html')


def csv_export(request):
    all_active_data = Employee.objects.filter(active=1)
    #print(all_active_data)
    #return HttpResponse(all_active_data)
    response = HttpResponse(content_type='text/csv')
    csv_writer = csv.writer(response)
    csv_writer.writerow(["Id","Name","Company","Salary","Designaion","DOJ","Active"])

    for emp in all_active_data.values_list('id','name','salary','company','designation','DOJ','active'):
        csv_writer.writerow(emp)
    
    response['Content-Disposition'] = 'attachment; filename="employee_data.csv"'
    return response


def upload_csv(request):
    template = "upload.html"
    data = Employee.objects.all()
    prompt = {
        'order': 'Order of the CSV should be name, salary, company, designation, DOJ, active',
        'profiles': data    
              }
    if request.method == "GET":
        return render(request, template, prompt)
    
    csv_file = request.FILES['csvfile']

    if not csv_file.name.endswith('csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    
    else:
    
      data_set = csv_file.read().decode('UTF-8')
      io_string = io.StringIO(data_set)
      next(io_string)

      for column in csv.reader(io_string, delimiter=',', quotechar="|"):
       created = Employee.objects.create(
        name=column[1],
        salary=column[2],
        company=column[3],
        designation=column[4],
        DOJ=column[5],
        active=column[6]
        
        )
        
    context = {
        'order': 'uploaded'  
    }
    return render(request, template, context)
	