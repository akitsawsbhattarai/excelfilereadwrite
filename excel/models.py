from django.db import models

# Create your models here.
class FileUploads(models.Model):
    file=models.FileField()