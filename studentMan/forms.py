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

class tiepNhanHSForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class themTaiKhoanGVForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'
      
class createUserStudent(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
