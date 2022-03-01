import imp
from django.http import HttpResponse
from django.shortcuts import render
from.models import FileUploads

# Create your views here.
def upload_file(request):
    if request.method=='POST':
        file2=request.FILES['file']
        document=FileUploads.objects.create(file=file2)
        document.save()
        return HttpResponse('file uploaded sucessfully')
    return render (request,'index.html')