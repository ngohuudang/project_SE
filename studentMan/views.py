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
from django.urls import reverse

from studentMan.models import Mark, Student
from .filters import *
from . forms import *
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
    marks = Mark.objects.all()
    myFilter = MarkFilter(request.GET, queryset=marks)
    marks = myFilter.qs
    context = {
        'marks':marks, 
        'myFilter': myFilter,
    }
    return render(request, 'admin_template/bangDiem.html',context=context)

def capNhatDiem(request, mark_id):
    mark= get_object_or_404(Mark, id=mark_id)
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
    return render(request,'admin_template/baoCaoMonHoc.html')

def baoCaoHK(request):
    return render(request,'admin_template/baoCaoHocKi.html')

def quanLiTuoi(request):
    return render(request, 'admin_template/quanLiTuoi.html')

def quanLiLop(request):
    return render(request,'admin_template/quanLiLop.html')

def quanLiMon(request):
    subjects = Subject.objects.all()
    context = {
        'subjects':subjects, 
    }
    return render(request,'admin_template/quanLiMon.html',context)