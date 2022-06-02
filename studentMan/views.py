from ast import Or
from curses.ascii import HT
from functools import total_ordering
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.urls import reverse

from .models import *
from .filters import *
from .forms import *


# Create your views here.

def admin_home(request):
    return render(request, 'admin_template/home_content.html')


def tiepNhanHS(request):
    return render(request, 'admin_template/tiepNhanHS.html')


def dsLop(request):
    return render(request, 'admin_template/dsLop.html')


def lapDSLop(request):
    return render(request, 'admin_template/lapDS.html')


def traCuu(request):
    myFilter = studentFilter()
    marks = Mark.objects.all()
    student = Student.objects.all()
    context = {"myFilter": myFilter,'marks':marks, 'student': student}
    return render(request, 'admin_template/traCuu.html', context)


def bangDiem(request):
    marks = Mark.objects.all()
    myFilter = MarkFilter(request.GET, queryset=marks)
    marks = myFilter.qs
    context = {
        'marks': marks,
        'myFilter': myFilter,
    }
    return render(request, 'admin_template/bangDiem.html', context=context)


def capNhatDiem(request, mark_id):
    mark = get_object_or_404(Mark, id=mark_id)
    form = transcriptForm(request.POST or None, instance=mark)
    context = {
        'form': form,
        'mark_id': mark_id,
        'page_title': 'capNhatDiem'
    }
    if request.method == 'POST':
        if form.is_valid():
            markFifteen = form.cleaned_data.get('markFifteen')
            markOne = form.cleaned_data.get('markOne')
            markFinal = form.cleaned_data.get('markFinal')

            try:
                mark = Mark.objects.get(id=mark.id)
                mark.markFifteen = markFifteen
                mark.markOne = markOne
                mark.markFinal = markFinal
                mark.save()
                messages.success(request, "Successfully Updated")
                return redirect(reverse('capNhatDiem', args=[mark_id]))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "admin_template/capNhatDiem.html", context)


def baoCaoMH(request):
    return render(request, 'admin_template/baoCaoMonHoc.html')


def baoCaoHK(request):
    return render(request, 'admin_template/baoCaoHocKi.html')


def quanLiTuoi(request,age_id):
    age = get_object_or_404(Age, id=age_id)
    form = AgeForm(request.POST or None, instance=age)
    context = {
        'form': form,
        'page_title': 'capNhatTuoi'
    }
    if request.method == 'POST':
        if form.is_valid():
            year = form.cleaned_data.get('year')
            max_age = form.cleaned_data.get('max_age')
            min_age = form.cleaned_data.get('min_age')
            try:
                age = Age.objects.get(id=Age.id)
                age.year = year
                age.max_age = max_age
                age.min_age = min_age
                age.save()
                messages.success(request, "Successfully Updated")
                return redirect(reverse('quanLiTuoi'))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "admin_template/quanLiTuoi.html", context)


def quanLiLop(request):
    return render(request, 'admin_template/quanLiLop.html')


def quanLiMon(request):
    subjects = Subject.objects.all()
    context = {
        'subjects': subjects,
    }
    return render(request, 'admin_template/quanLiMon.html', context)


def capNhatMon(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    form = subjectForm(request.POST or None, instance=subject)
    context = {
        'form': form,
        'subject_id': subject_id,
        'page_title': 'capNhatMon'
    }
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            approved_mark = form.cleaned_data.get('approved_mark')
            try:
                subject = Subject.objects.get(id=subject.id)
                subject.name = name
                subject.approved_mark = approved_mark
                subject.save()
                messages.success(request, "Successfully Updated")
                return redirect(reverse('capNhatMon', args=[subject_id]))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "admin_template/capNhatMon.html", context)


def xoaMon(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    subject.delete()
    messages.success(request, "Subject deleted successfully!")
    return redirect(reverse('quanLiMon'))


def themMon(request):
    form = subjectForm(request.POST or None)
    context = {
        'form': form,
        'page_title': 'themMon'
    }
    if request.method == 'POST':
        if form.is_valid():
            SubjectID = form.cleaned_data.get('SubjectID')
            name = form.cleaned_data.get('name')
            approved_mark = form.cleaned_data.get('approved_mark')
            try:
                subject = Subject()
                subject.SubjectID = SubjectID
                subject.name = name
                subject.approved_mark = approved_mark
                subject.save()
                messages.success(request, "Successfully Added")
                return redirect(reverse('themMon'))
            except:
                messages.error(request, "Could Not Add")
        else:
            messages.error(request, "Could Not Add")
    return render(request, 'admin_template/themMon.html', context)
