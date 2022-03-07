from django.db import models

# Create your models here.
class Grade(models.Model):
    student_name = models.CharField(max_length=50)
    semester =  models.CharField(max_length=20)
    subject1_name =models.CharField(max_length=50)
    subject2_name =models.CharField(max_length=50)
    subject3_name= models.CharField(max_length=50)
    subject4_name= models.CharField(max_length=50, blank=True, null=True)
    subject5_name= models.CharField(max_length=50, blank=True, null=True)

    subject1_code =models.CharField(max_length=50)
    subject2_code =models.CharField(max_length=50)
    subject3_code= models.CharField(max_length=50)
    subject4_code= models.CharField(max_length=50, blank=True, null=True)
    subject5_code= models.CharField(max_length=50, blank=True, null=True)

    subject1_credit_hour =models.IntegerField()
    subject2_credit_hour =models.IntegerField()
    subject3_credit_hour= models.IntegerField()
    subject4_credit_hour= models.IntegerField( blank=True, null=True)
    subject5_credit_hour= models.IntegerField( blank=True, null=True)

    subject1_marks =models.CharField(max_length=50)
    subject2_marks =models.CharField(max_length=50)
    subject3_marks= models.CharField(max_length=50)
    subject4_marks= models.CharField(max_length=50, blank=True, null=True)
    subject5_marks= models.CharField(max_length=50, blank=True, null=True)



# class FileUploads(models.Model):
#     title=models.CharField(max_length=20)
#     file=models.FileField(validators=[FileExtensionValidator(['xlsx', 'xls'])])