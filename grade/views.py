from django.shortcuts import render
from .forms import ExceldataForm

import pandas as pd
import xlrd
from .models import Grade

# Create your views here.
def excel_upload(request):
    form=ExceldataForm()
    if request.method=="POST":
        form=ExceldataForm(request.POST,request.FILES)

        if form.is_valid():
            excel_file = form.cleaned_data['file']
            print (excel_file)
            df=pd.read_excel(excel_file)
            print (df)
            print (df.columns)
            for i in df.index:
                
                student_name = (df['Students Name'][i])
                # yo k gareko
                #grade ko object create garna sabai value pathaunu pardaina euta euta pathauna milxa tw


                subject_name =(df['Subject Name'][i])

                # c= (df['Code'][i])
                # Code= Grade.objects.create(c)
                # Code.save()

                # d= (df['Credit Hour'][i])
                # CreditHour= Grade.objects.create(d)
                # CreditHour.save()

                # e= df['Marks Obtained'][i]
                # MarksObtained= Grade.objects.create(e)
                # MarksObtained.save()

                # f= (df['Subject Name.1'][i])
                # SubjectName1= Grade.objects.create(f)
                # SubjectName1.save()

                # g= (df['Code.2'][i])
                # Code2= Grade.objects.create(g)
                # Code2.save()

                # h= (df['Credit Hour.2'][i])
                # CreditHour2= Grade.objects.create(h)
                # CreditHour2.save()

                # i= (df['Marks Obtained.2'][i])
                # MarksObtained2= Grade.objects.create(i)
                # MarksObtained2.save()

                # j= (df['Subject Name.3'][i])
                # SubjectName3= Grade.objects.create(j)
                # SubjectName3.save()

                # k= (df['Code.3'][i])
                # Code3= Grade.objects.create(k)
                # Code3.save()

                # l= (df['Credit Hour.3'][i])
                # CreditHour3= Grade.objects.create(l)
                # CreditHour3.save()

                
                # m= (df['Marks Obtained.3'][i])
                # MarksObtained3= Grade.objects.create(m)
                # MarksObtained3.save()

                # n= (df['Subject Name.4'][i])
                # SubjectName4= Grade.objects.create(n)
                # SubjectName4.save()

                # o= (df['Code.4'][i])
                # Code4= Grade.objects.create(o)
                # Code4.save()

                
                # p= (df['Credit Hour.4'][i])
                # CreditHour4= Grade.objects.create(p)
                # CreditHour4.save()

                # q= (df['Marks Obtained.4'][i])
                # MarksObtained4= Grade.objects.create(q)
                # MarksObtained4.save()
                print(student_name, subject_name)
                grade = Grade.objects.create(student_name = student_name)


    
    context={
        'form':form
    }
    return render(request, 'form.html', context)