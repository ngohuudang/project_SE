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
from .report import *

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


def baoCaoMH(request):
    return render(request, 'admin_template/baoCaoMonHoc.html')


@unauthenticated_user
def baoCaoHocKy(request, lop, hocKy, nienKhoa):
    all_classes = ClassOfSchool.objects.all()
    id = request.user.username
    report = Report()
    report1 = [report.show(id, lop, hocKy, nienKhoa)]
    all_nienKhoa = Age.objects.all()
    context = {'reports': report1,
               'classes': all_classes,
               'lop': lop,
               'hocky': hocKy,
               'nienKhoa': nienKhoa,
               'all_nienKhoa': all_nienKhoa}

    return render(request, 'admin_template/baoCaoHocKi.html', context)


def baoCaoHK(request):
    return baoCaoHocKy(request, "---", 1, 2020)


def quanLiTuoi(request):
    return render(request, 'admin_template/quanLiTuoi.html')


def quanLiLop(request):
    return render(request, 'admin_template/quanLiLop.html')


def quanLiMon(request):
    return render(request, 'admin_template/quanLiMon.html')
