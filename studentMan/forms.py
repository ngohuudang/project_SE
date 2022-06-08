from matplotlib import widgets
from .models import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'

class transcriptForm(forms.ModelForm):
    class Meta:
        model = Mark
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



class CreateClassForm(forms.ModelForm):
    class_choices = set([(c.classId, c.classId) for c in ClassOfSchool.objects.all()])
    classOfSchool = forms.CharField(label="",widget=forms.Select(
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


class CustomUserForm(forms.ModelForm):
    username = forms.CharField(label="",widget=forms.TextInput(
        attrs={'id':"username_user", 'class':"form-control"
    }))

    password = forms.CharField(label="",widget=forms.TextInput(
        attrs={'id':"password_user", 'class':"form-control"
    }))

    name = forms.CharField(label='', widget=forms.TextInput(
        attrs={'id':"name_user", 'class':"form-control"
    }))
    dateOfBirth = forms.CharField(label="",widget=forms.DateInput(
        attrs={'type': 'date', 'id':"datepicker", 'class': 'form-control' 
    }))

    sex = forms.CharField(label="",widget=forms.Select(
        choices=CustomUser().SEX_CATELOGY, 
        attrs={'class': 'form-select', 'id': 'sex_user'
    }))

    email = forms.CharField(label="",widget=forms.TextInput(
        attrs={'type': 'email', 'id':'email_user', 'class': 'form-control',
    }))

    address = forms.CharField(label="",widget=forms.Textarea(
        attrs={"rows":4, 'class': 'form-control', 'id': 'address_user', 
            'placeholder':"12, đường 01, quận 1, tp HCM"
    }))


    phone = forms.CharField(label="",widget=forms.TextInput(
        attrs={'id':'phone_user', 'class': 'form-control',
    }))

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)

        if kwargs.get('instance'):
            instance = kwargs.get('instance').admin.__dict__
            self.fields['password'].required = False
            for field in CustomUserForm.Meta.fields:
                self.fields[field].initial = instance.get(field)

    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'name', 'dateOfBirth', 'sex', 'email','address', 'phone']

class HiddenUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        exclude = ['username', 'password', 'name', 'dateOfBirth', 'sex', 'email','address', 'phone']

class AdminForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(AdminForm, self).__init__(*args, **kwargs)
    class Meta:
        model = Admin
        fields = CustomUserForm.Meta.fields

class TeacherForm(CustomUserForm):
    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        self.fields['subject'].required = False
        self.fields['classOfSchool'].required = False
        self.fields['subject'].widget.attrs.update({'class': 'form-select'})
        self.fields['classOfSchool'].widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Teacher
        fields = CustomUserForm.Meta.fields +  ['subject', 'classOfSchool']

class StudentForm(CustomUserForm):
    class_choices = {(None, '-----')}
    class_choices.update(set([(c.classId, c.classId) for c in ClassOfSchool.objects.all()]))
    classOfSchool = forms.CharField(label="",widget=forms.Select(
        choices=class_choices, 
        attrs={'class': 'form-select'
    }), required = False)
    
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['classOfSchool'].required = False
        self.fields['classOfSchool'].widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Student
        fields = CustomUserForm.Meta.fields +  ['classOfSchool']
        # widgets = {
        #     'classOfSchool': forms.Select()
        # }