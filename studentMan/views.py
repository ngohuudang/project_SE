from functools import total_ordering
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import *
from numpy import round_
from .report import *

from .decorators import unauthenticated_user

from django.contrib.auth.models import Group

from django.urls import reverse

from studentMan.models import Mark, Student
from .filters import *
from . forms import *

semester =2
# Create your views here.

@login_required(login_url='login')
def admin_home(request):
    total_teachers = Teacher.objects.all().count()
    total_students = Student.objects.all().count()
    total_subjects = Subject.objects.all().count()
    total_classes = ClassOfSchool.objects.all().count()
    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_subjects': total_subjects,
        'total_classes': total_classes,
    }
    return render(request, 'admin_template/home_content.html',context=context)


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

def dsTaiKhoan(request):
    return render(request, 'admin_template/dsTaiKhoan.html')



def dsLop(request):
    students = Student.objects.all()
    classFilter = ClassFilter(request.GET, queryset=students)
    students = classFilter.qs
    context = {
        'students':students, 
        'classFilter': classFilter,
    }
    return render(request, 'admin_template/dsLop.html', context=context)


def lapDSLop(request):
    students = Student.objects.filter(classOfSchool__classId =None)
    form = CreateClassForm()
    if request.method == 'POST':
        id_list = request.POST.getlist('docid')
        cl = request.POST.get('classOfSchool')
        class_list = ClassOfSchool.objects.all()
        for classOfSchool in class_list:
            if classOfSchool.classId == cl:
                studentsInClass = Student.objects.filter(classOfSchool__classId =cl)
                if classOfSchool.max_number >= (len(studentsInClass) + len(id_list)):
                    for id in id_list:
                        student = Student.objects.get(StudentID=id)
                        student.classOfSchool = classOfSchool
                        student.save()
                    messages.success(request, "Thêm thành công")
                else:
                    messages.success(request, "Số lượng học sinh vượt quá qui định")

    context = {
        'students':students, 
        'form': form,
    }
    return render(request, 'admin_template/lapDS.html',context=context)


def traCuu(request):
    marks = Mark.objects.all()
    marksFilter = StudentInMarkFilter(request.GET, queryset=marks)
    marks = marksFilter.qs
    students = set([mark.student for mark in marks])
    avgMarks1 = []
    avgMarks2 = []
    for mark in marks:
        if mark.semester_mark == '1':
            if (mark.markFifteen != None) and (mark.markOne != None) and (mark.markFinal != None):
                avgMarks1.append(round((mark.markFifteen + 2*mark.markOne + 3*mark.markFinal)/6, 2))
            else:
                avgMarks1.append(None)
        elif mark.semester_mark == '2':
            if (mark.markFifteen != None) and (mark.markOne != None) and (mark.markFinal != None):
                avgMarks2.append(round((mark.markFifteen + 2*mark.markOne + 3*mark.markFinal)/6, 2))
            else:
                avgMarks2.append(None)
    marks = zip(students, avgMarks1, avgMarks2)
    context = {
        'marks': marks,
        'marksFilter': marksFilter
    }
    return render(request, 'admin_template/traCuu.html',context=context)


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
    return render(request, 'admin_template/baoCaoMonHoc.html')


@unauthenticated_user
# def baoCaoHocKy(request, lop, hocKy, nienKhoa):
#     all_classes = ClassOfSchool.objects.all()
#     id = request.user.username
#     report = Report()
#     report1 = [report.show(id, lop, hocKy, nienKhoa)]
#     all_nienKhoa = Age.objects.all()
#     context = {'reports': report1,
#                'classes': all_classes,
#                'lop': lop,
#                'hocky': hocKy,
#                'nienKhoa': nienKhoa,
#                'all_nienKhoa': all_nienKhoa}

#     return render(request, 'admin_template/baoCaoHocKi.html', context)

def baoCaoHocKy(request, lop, hocKy, nienKhoa):
    all_classes = ClassOfSchool.objects.all()
    # print('all_classes',all_classes)
    id = request.user.id
    report = Report()
    report1 = [report.show(id, lop, hocKy, nienKhoa)]
    all_nienKhoa = Age.objects.all()
    context = {
        'reports': report1, 
        'classes': all_classes,
        'lop': lop,
        'hocky': hocKy,
        'nienKhoa': nienKhoa,
        'all_nienKhoa': all_nienKhoa
    }

    return render(request, 'admin_template/baoCaoHocKi.html', context)

def baoCaoHK(request):
    return baoCaoHocKy(request, '---', '1', '2021-2022')


def quanLiTuoi(request):
    return render(request, 'admin_template/quanLiTuoi.html')


def quanLiLop(request):
    classes = ClassOfSchool.objects.all()
    yearFilter = YearFilter(request.GET, queryset=classes)
    classes = yearFilter.qs
    context = {
        'classes': classes,
        'yearFilter':yearFilter
    }
    return render(request,'admin_template/quanLiLop.html',context= context)

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
            classId = form.cleaned_data.get('classId')
            year = form.cleaned_data.get('year')
            max_number = form.cleaned_data.get('max_number')
            try:
                Class = ClassOfSchool()
                Class.classId = classId
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


def quanLiMon(request):
    subjects = Subject.objects.all()
    context = {
        'subjects':subjects, 
    }
    return render(request,'admin_template/quanLiMon.html',context)

def capNhatMon(request, subject_id):
    subject= get_object_or_404(Subject, id=subject_id)
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
                students = Student.objects.all()
                for student in students:
                    for semester_mark in range(1,semester+1):
                        mark = Mark()
                        mark.student = student
                        mark.subject = subject
                        mark.semester_mark = semester_mark
                        mark.save()
                messages.success(request, "Successfully Added")
                return redirect(reverse('themMon'))
            except:
                messages.error(request, "Could Not Add")
        else:
            messages.error(request, "Could Not Add")
    return render(request, 'admin_template/themMon.html', context)
