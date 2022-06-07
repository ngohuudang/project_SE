from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
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


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CreateClassForm(forms.ModelForm):
    class_choices = set([(c.classId, c.classId) for c in ClassOfSchool.objects.all()])
    classOfSchool = forms.CharField(label="", widget=forms.Select(
        choices=class_choices,
        attrs={'class': 'form-select'
               }))

    class Meta:
        model = ClassOfSchool
        fields = []


class classForm(forms.ModelForm):
    class Meta:
        model = ClassOfSchool
        fields = '__all__'


class ageForm(forms.ModelForm):
    class Meta:
        model = Age
        fields = '__all__'


class studentUpdateForm(forms.ModelForm):
    SEX_CATELOGY = (
        ('nam', 'nam'),
        ('nu', 'nu')
    )
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.TypedChoiceField(choices=SEX_CATELOGY,widget=forms.TextInput(attrs={'class': 'form-control'}))
    dateOfBirth = forms.DateTimeField()
    phone = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['classOfSchool', 'StudentID', 'year']


class teacherUpdateForm(forms.ModelForm):
    SEX_CATELOGY = (
        ('nam', 'nam'),
        ('nu', 'nu')
    )
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    sex = forms.TypedChoiceField(choices=SEX_CATELOGY,widget=forms.TextInput(attrs={'class': 'form-control'}))
    dateOfBirth = forms.DateTimeField()
    phone = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Teacher
        fields = '__all__'
        exclude = ['classOfSchool', 'TeacherID', 'year']
