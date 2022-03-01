import imp
from logging.config import valid_ident
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from.models import FileUploads
import pandas as pd
from.form import FileuploadForm



# Create your views here.
def home(request):
    data=FileUploads.objects.all()
    context={
        'data':data
    }
   
    return render(request,'home.html',context)

def upload_file(request):
    form=FileuploadForm()
    if request.method=='POST':
        form=FileuploadForm(request.POST,request.FILES)
        
        if form.is_valid():
            form.save()
            redirect('excel:home')
    context={
            'form':form
        }
    return render (request,'index.html',context)

