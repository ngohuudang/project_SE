from ast import Or
from curses.ascii import HT
from functools import total_ordering
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .models import *
from django.forms import ModelForm
from django import forms
from . forms import *
from django.urls import reverse
# Create your views here.

def admin_home(request):
    return render(request, 'admin_template/home_content.html')

def tiepNhanHS(request):
    return render(request, 'admin_template/tiepNhanHS.html')

def dsLop(request):
    dsLop = Student.objects.all()
    classes = ClassOfSchool.objects.all()
    context = {
        'classes': classes,
        'dsLop': dsLop,
    }
    return render(request=request, template_name='admin_template/dsLop.html', context=context)

def dsLopFilter(request,pk_test):
    dsLopFilter = Student.objects.filter(ClassOfSchool__ClassId=pk_test)
    return render(request=request, template_name='admin_template/dsLop.html', context={'dsLopFilter': dsLopFilter})

def lapDSLop(request):
    lapDsLop = Student.objects.filter(ClassOfSchool__isnull=True)
    return render(request=request,template_name='admin_template/lapDS.html', context={'lapDsLop': lapDsLop})

def traCuu(request):
    return render(request,'admin_template/traCuu.html')

def bangDiem(request):
    return render(request, 'admin_template/bangDiem.html')

def baoCaoMH(request):
    return render(request,'admin_template/baoCaoMonHoc.html')

def baoCaoHK(request):
    return render(request,'admin_template/baoCaoHocKi.html')

def quanLiTuoi(request):
    return render(request, 'admin_template/quanLiTuoi.html')

def quanLiLop(request):
    classes = ClassOfSchool.objects.all()
    nienkhoa = Age.objects.all()
    context = {
        'classes': classes,
        'nienkhoa':nienkhoa
    }
    return render(request,'admin_template/quanLiLop.html',context)

def quanLiLopFilter(request,pk_test):
    quanLiLopFilter = ClassOfSchool.objects.filter(year__year=pk_test)
    return render(request=request, template_name='admin_template/quanLiLop.html', context={'quanLiLopFilter': quanLiLopFilter})

def quanLiMon(request):
    return render(request,'admin_template/quanLiMon.html')

def capNhatLop(request, class_id):
    Class = get_object_or_404(ClassOfSchool, id=class_id)
    form = classForm(request.POST or None, instance=Class)
    context = {
        'form': form,
        'page_title': 'capNhatLop'
    }
    if request.method == 'POST':
        if form.is_valid():
            ClassId = form.cleaned_data.get('ClassId')
            year = form.cleaned_data.get('year')
            max_number = form.cleaned_data.get('max_number')
            try:
                Class = ClassOfSchool.objects.get(id=Class.id)
                Class.ClassId = ClassId
                Class.year = year
                Class.max_number = max_number
                Class.save()
                messages.success(request, "Successfully Updated")
                return redirect(reverse('quanLiLop'))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Please Fill Form Properly!")
    else:
        return render(request, "admin_template/capNhatLop.html", context)


def xoaLop(request, class_id):
    Class = get_object_or_404(ClassOfSchool, id=class_id)
    Class.delete()
    messages.success(request, "Class deleted successfully!")
    return redirect(reverse('quanLiLop'))


def themLop(request):
    form = classForm(request.POST or None)
    context = {
        'form': form,
        'page_title': 'themLop'
    }
    if request.method == 'POST':
        if form.is_valid():
            ClassId = form.cleaned_data.get('ClassId')
            year = form.cleaned_data.get('year')
            max_number = form.cleaned_data.get('max_number')
            try:
                Class = ClassOfSchool()
                Class.ClassId = ClassId
                Class.year = year
                Class.max_number = max_number
                Class.save()
                messages.success(request, "Successfully Added")
                return redirect(reverse('quanLiLop'))
            except:
                messages.error(request, "Could Not Add")
        else:
            messages.error(request, "Could Not Add")
    return render(request, 'admin_template/themLop.html', context)