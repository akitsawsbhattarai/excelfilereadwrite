from django.forms import ModelForm
from .models import FileUploads

class FileuploadForm(ModelForm):
    class Meta():
        model=FileUploads
        fields=['title','file']