from logging import Filter
from random import choices
from re import A
import django_filters
from django_filters import CharFilter, ChoiceFilter

from .models import *


class MarkFilter(django_filters.FilterSet):
    class_list = set([mark.student.classOfSchool for mark in Mark.objects.all()])
    class_choices = [(c, c) for c in class_list]
    student = ChoiceFilter(label='Lớp', choices=class_choices, method='filter_by_class')

    subject_list = set([mark.subject.name for mark in Mark.objects.all()])
    subject_choices = [(s, s) for s in subject_list]
    subject = ChoiceFilter(label='Môn học', choices=subject_choices, method='filter_by_subject')
    SEMESTER_CATEGORY = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    )
    semester_mark = ChoiceFilter(label='Học kì', choices=SEMESTER_CATEGORY, method='filter_by_semester')

    class Meta:
        model = Mark
        fields = ['student', 'subject', 'semester_mark']

    def filter_by_class(self, queryset, name, value):
        return queryset.filter(student__classOfSchool__classId=value)

    def filter_by_subject(self, queryset, name, value):
        return queryset.filter(subject__name=value)

    def filter_by_semester(self, queryset, name, value):
        return queryset.filter(semester_mark=value)

    # def __init__(self, *args, **kwargs):
    #     super(MarkFilter).__init__(*args, **kwargs)
    #     self.fields['semester_mark'].widget.attrs.update(
    #         {'class': 'form-select'}
    #     )


class studentFilter(django_filters.FilterSet):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['StudentID', 'sex', 'dateOfBirth', 'phone',
                   'email', 'address', 'user', 'year']
