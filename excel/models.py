from django.db import models

class FileUploads(models.Model):
    title=models.CharField(max_length=20)
    file=models.FileField()