from logging import Filter
from random import choices
from re import A
import django_filters
from django_filters import CharFilter,ChoiceFilter

from .models import *
from django import forms
class MarkFilter(django_filters.FilterSet):
    class_list = set([mark.student.classOfSchool for mark in Mark.objects.all() if mark.student.classOfSchool is not None])
    class_choices = [(c,c) for c in class_list]
    student = ChoiceFilter(
        label= '',
        choices = class_choices, 
        method= 'filter_by_class',
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    subject_list = set([mark.subject.name for mark in Mark.objects.all()])
    subject_choices = [(s,s) for s in subject_list]
    subject = ChoiceFilter(
        label= 'Môn học',
        choices = subject_choices, 
        method= 'filter_by_subject',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    SEMESTER_CATEGORY = (
        ('1', '1'),
        ('2', '2')
    )
    semester_mark = ChoiceFilter(
        label= 'Học kì',
        choices = SEMESTER_CATEGORY, 
        method= 'filter_by_semester',
        widget=forms.Select(attrs={'class': 'form-select'})
    )


    class Meta:
        model = Mark
        fields = ['student','subject','semester_mark']
    def filter_by_class(self, queryset, name, value):
        return queryset.filter(student__classOfSchool__classId =value)

    def filter_by_subject(self, queryset, name, value):
        return queryset.filter(subject__name =value)

    def filter_by_semester(self, queryset, name, value):
        return queryset.filter(semester_mark =value)

class StudentInMarkFilter(django_filters.FilterSet):
    name = CharFilter(
        field_name='student__name', 
        label = '', 
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        lookup_expr='icontains'
    )
    class_list = set([mark.student.classOfSchool for mark in Mark.objects.all() if mark.student.classOfSchool is not None])
    class_choices = [(c,c) for c in class_list]
    classOfSchool = ChoiceFilter(
        label= '',
        choices = class_choices, 
        method= 'filter_by_class',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    class Meta:
        model = Mark
        fields = []
    
    def filter_by_class(self, queryset, name, value):
        return queryset.filter(student__classOfSchool__classId =value)