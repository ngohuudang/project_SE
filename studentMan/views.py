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
from django.contrib.auth.models import Group
# Create your views here.

def admin_home(request):
    return render(request, 'admin_template/home_content.html')

def tiepNhanHS(request):
    return render(request, 'admin_template/tiepNhanHS.html')

def dsLop(request):
    return render(request, 'admin_template/dsLop.html')

def lapDSLop(request):
    return render(request,'admin_template/lapDS.html')

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
    return render(request,'admin_template/quanLiLop.html')

def quanLiMon(request):
    return render(request,'admin_template/quanLiMon.html')