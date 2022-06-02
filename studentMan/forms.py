from django import forms
from .models import *

class classForm(forms.ModelForm):
    class Meta:
        model = ClassOfSchool
        fields = '__all__'