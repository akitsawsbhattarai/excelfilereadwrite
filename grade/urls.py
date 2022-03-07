from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from grade.views import excel_upload

app_name='grade'
urlpatterns = [
    path('uploadexcel/', excel_upload, name='excel_upload'),
    
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
