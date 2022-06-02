from attr import field
from django.forms import ModelForm
from .models import *
from django import forms


class transcriptForm(forms.ModelForm):
    class Meta:
        model = Mark
        # fields = ['student','subject','semester_mark']
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['semester_mark'].widget.attrs.update(
            {'class': 'form-select'}
        )


class subjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class AgeForm(forms.ModelForm):
    class Meta:
        model = Age
        fields = '__all__'
