from ast import Or
from curses.ascii import HT
from functools import total_ordering
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import *
from .report_child_classes import *

from .decorators import unauthenticated_user

from django.contrib.auth.models import Group


# Create your views here.

@login_required(login_url='login')
def admin_home(request):
    return render(request, 'admin_template/home_content.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_home')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'admin_template/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def tiepNhanHS(request):
    return render(request, 'admin_template/tiepNhanHS.html')


def dsLop(request):
    return render(request, 'admin_template/dsLop.html')


def lapDSLop(request):
    return render(request, 'admin_template/lapDS.html')


def traCuu(request):
    return render(request, 'admin_template/traCuu.html')


def bangDiem(request):
    return render(request, 'admin_template/bangDiem.html')


def baoCaoMonHoc(request, lop, mon, hocKy, nienKhoa):
    all_classes = Subject_Report().remove_duplicate(ClassOfSchool.objects.all())
    subjects = Subject.objects.all()
    years = Age.objects.all()
    id = request.user.username
    reports = Subject_Report().report_to_show(id, lop, mon, hocKy, nienKhoa)
    context = {'reports': reports,
               'classes': all_classes,
               'current_class': lop,
               'semester': hocKy,
               'years': years,
               'year': nienKhoa,
               'subjects': subjects,
               'subject': mon}
    return render(request, 'admin_template/baoCaoMonHoc.html', context)


def baoCaoMH(request):
    years = Age.objects.all()
    current_year = years.aggregate(Max('year'))
    return baoCaoMonHoc(request, '---', '---', 1, current_year['year__max'])


@unauthenticated_user
def baoCaoHocKy(request, lop, hocKy, nienKhoa):
    all_classes = Semester_Report().remove_duplicate(ClassOfSchool.objects.all())
    subject_num = len(Subject.objects.all())
    id = request.user.username
    reports = Semester_Report().report_to_show(id, lop, hocKy, nienKhoa, subject_num)
    all_nienKhoa = Age.objects.all()
    context = {'reports': reports,
               'classes': all_classes,
               'lop': lop,
               'hocky': hocKy,
               'nienKhoa': nienKhoa,
               'all_nienKhoa': all_nienKhoa}

    return render(request, 'admin_template/baoCaoHocKi.html', context)


def baoCaoHK(request):
    years = Age.objects.all()
    current_year = years.aggregate(Max('year'))
    return baoCaoHocKy(request, "---", 1, current_year['year__max'])


def quanLiTuoi(request):
    return render(request, 'admin_template/quanLiTuoi.html')


def quanLiLop(request):
    return render(request, 'admin_template/quanLiLop.html')


def quanLiMon(request):
    return render(request, 'admin_template/quanLiMon.html')
