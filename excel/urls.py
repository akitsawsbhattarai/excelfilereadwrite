from django.urls import path
from .views import upload_file
from django.conf.urls.static import static
from django.conf import settings

app_name='excel'
urlpatterns = [
    path('upload/', upload_file,name='upload'),
   
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
