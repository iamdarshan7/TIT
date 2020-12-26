from django import forms
from .models import Data

class FormDatas(forms.ModelForm):
    class Meta:
        model = Data
        fields = ('name', 'email', 'phone', 'program', 'percentage')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name', 'name':'dzother[Name]','id':'id_name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email Address', 'name': 'dzother[Email]','id':'id_email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone', 'name': 'dzother[Phone]','id':'id_phone'}),
        }


# class AnotherFormDatas(forms.ModelForm):
#     class Meta:
#         model = AnotherData
#         fields = ('location', 'stream', 'college', 'university')        