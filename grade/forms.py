from django.forms import forms, fields
from django.core.validators import FileExtensionValidator

class ExceldataForm(forms.Form):
    file= fields.FileField()

    
class ExcelUpload(forms.Form):
    file = fields.FileField(validators=[FileExtensionValidator(['xlsx', 'xls'])])