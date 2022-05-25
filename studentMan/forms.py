from django.forms import ModelForm
from .models import *
from django import forms

# class transcriptForm(forms.ModelForm):
#     class Meta:
#         model = Mark
#         fields = ['student','subject','semester_mark']

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['semester_mark'].widget.attrs.update(
#             {'class': 'form-select'}
#         )
