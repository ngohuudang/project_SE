from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.forms import *
from .report import *
from datetime import datetime
from .decorators import unauthenticated_user
import numpy as np
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from .filters import *
from .forms import *
from .models import *
from .report_child_classes import *
semester = 2


# Create your views here.

@login_required(login_url='login')
def admin_home(request):
    total_admins = Admin.objects.all().count()
    total_teachers = Teacher.objects.all().count()
    total_students = Student.objects.all().count()
    total_subjects = Subject.objects.all().count()
    total_classes = ClassOfSchool.objects.all().count()
    total_classes = ClassOfSchool.objects.all().count()

    context = {
        'total_students': total_students,
        'total_teachers': total_teachers,
        'total_admins': total_admins,
        'total_subjects': total_subjects,
        'total_classes': total_classes,
    }
    return render(request, 'admin_template/home_content.html', context=context)


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


@login_required(login_url='login')
def capNhatTaiKhoan(request):
    if request.method == 'POST':
        profile_form = userUpdateForm(request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Cập nhật thành công')
            return redirect(to='capNhatTaiKhoan')
    else:
        profile_form = userUpdateForm(instance=request.user)

    return render(request, 'admin_template/capNhatTaiKhoan.html', {'profile_form': profile_form})



class doiMatKhau(SuccessMessageMixin, PasswordChangeView):
    template_name = 'admin_template/capNhatMatKhau.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('capNhatTaiKhoan')

def logoutUser(request):
    logout(request)
    return redirect('login')


def themAdmin(request):
    form = AdminForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            sex = form.cleaned_data.get('sex')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            try:
                admin = Admin()
                user = CustomUser.objects.create_superuser(
                    username = username, password= password, name = name,
                    dateOfBirth = datetime.strptime(dateOfBirth,'%Y-%m-%d'),
                    sex = sex, email = email, phone = phone, address = address)
                user.save()
                admin.user = user
                admin.save()
                messages.success(request, "Thêm thành công")
                return redirect(reverse('dsTaiKhoan'))
            except:
                messages.error(request, "Không thể thêm")
        else:
            messages.error(request, "Dữ liệu không phù hợp")
    return render(request, 'admin_template/themAdmin.html', context=context)

def themGV(request):
    form = TeacherForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            sex = form.cleaned_data.get('sex')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            subject = form.cleaned_data.get('subject')
            classOfSchool = form.cleaned_data.get('classOfSchool')
            try:
                user = CustomUser.objects.create_user(
                    username = username, password= password, name = name, role ='2',
                    dateOfBirth = datetime.strptime(dateOfBirth,'%Y-%m-%d'),
                    sex = sex, email = email, phone = phone, address = address)
                teacher = Teacher(user = user)
                if subject:
                    teacher.subject = subject
                teacher.save()
                for c  in classOfSchool:
                    teacher.classOfSchool.add(c)
                teacher.save()
                messages.success(request, "Thêm thành công")
                return redirect(reverse('dsTaiKhoan'))
            except:
                messages.error(request, "Không thể thêm")
        else:
            messages.error(request, "Dữ liệu không phù hợp")
    return render(request, 'admin_template/themGV.html', context=context)


# def khoiTaoDiem(student, classOfSchool):
#     student.

def tiepNhanHS(request):
    form = StudentForm(request.POST or None)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            name = form.cleaned_data.get('name')
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            sex = form.cleaned_data.get('sex')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            # classOfSchool = form.cleaned_data.get('classOfSchool')
            try:
                user = CustomUser.objects._create_user(
                    username = username, password= password, name = name, role ='3',
                    dateOfBirth = datetime.strptime(dateOfBirth,'%Y-%m-%d'),
                    sex = sex, email = email, phone = phone, address = address)
                student = Student(user = user)
                student.save()
                # c = ClassOfSchool.objects.get(classId = classOfSchool)
                # student.classOfSchool.add(c)
                # student.save()
                # for subject in Subject.objects.all():
                #     c.year.year
                messages.success(request, "Thêm thành công")
            except:
                messages.error(request, "Không thể thêm")
        else:
            messages.error(request, "Dữ liệu không phù hợp")
    return render(request, 'admin_template/tiepNhanHS.html',context=context)


def dsTaiKhoan(request):
    return render(request, 'admin_template/dsTaiKhoan.html')


def dsLop(request):
    students = Student.objects.all().order_by('user__name')
    classFilter = ClassFilter(request.GET, queryset=students)
    students = classFilter.qs.order_by('user__name')
    context = {
        'students': students,
        'classFilter': classFilter,
    }
    return render(request, 'admin_template/dsLop.html', context=context)

def chonNienKhoaLop(request):
    form = YearForm()
    age = Age.objects.all()
    context = {
        'form': form,
        'age': age
    }
    return render(request, 'admin_template/chonNienKhoaLop.html', context=context)


def lapDSLop(request,age_id):
    year = Age.objects.get(id =age_id)
    student_with_year = []
    for student in Student.objects.all():
        for c in student.classOfSchool.all():
            if c.year ==year:
                student_with_year.append(student)
                break
    student_dont_with_year =[]
    for student in Student.objects.all():
        if student not in student_with_year:
            student_dont_with_year.append(student)
    form = CreateClassForm(request.POST, age_id = age_id)

    if request.method == 'POST':
        usernames = request.POST.getlist('username_class')
        cl = request.POST.get('classOfSchool')
        class_list = ClassOfSchool.objects.all()
        for classOfSchool in class_list:
            if classOfSchool.classId == cl:
                studentsInClass = Student.objects.filter(classOfSchool__classId=cl)
                if classOfSchool.max_number >= (len(studentsInClass) + len(usernames)):
                    for username in usernames:
                        student = Student.objects.get(user__username=username)
                        student.classOfSchool.add(classOfSchool)
                        student.save()
                    messages.success(request, "Thêm thành công")
                    return redirect(reverse('lapDSLop', kwargs={'age_id':age_id}))
                else:
                    messages.success(request, "Số lượng học sinh vượt quá qui định")
    context = {
        'students': student_dont_with_year,
        'form': form,
    }
    return render(request, 'admin_template/lapDS.html', context=context)

def trungBinhMon(subject, student):
    for mark in Mark.objects.filter(student = student).filter(subject = subject):
        if mark.semester_mark == '1':
            avgMarks1 = round((mark.markFifteen + 2 * mark.markOne + 3 * mark.markFinal) / 6, 2)
        else:
            avgMarks2 = round((mark.markFifteen + 2 * mark.markOne + 3 * mark.markFinal) / 6, 2)
    return avgMarks1, avgMarks2


def chonNienKhoaTraCuu(request):
    form = YearForm()
    age = Age.objects.all()
    context = {
        'form': form,
        'age': age
    }
    return render(request, 'admin_template/chonNienKhoaTraCuu.html', context=context)

def traCuu(request,age_id):
    year = Age.objects.get(id =age_id)
    marks = Mark.objects.filter(subject__year= year)
    marksFilter = StudentInMarkFilter(request.GET, queryset=marks)
    marks = marksFilter.qs.order_by('student__user__name')
    students = []
    avgMarks1 = []
    avgMarks2 = []
    classOfSchool = []
    marks_in_year = marks
    students_in_year = set([mark.student for mark in marks_in_year])
    for student in students_in_year:
        students.append(student)
        subjects_in_year = set([mark.subject for mark in marks_in_year])
        m = [trungBinhMon(subject, student) for subject in subjects_in_year]
        avg = np.mean(np.array(m), axis=0)
        avgMarks1.append(avg[0])
        avgMarks2.append(avg[1])
        for c in student.classOfSchool.all():
            if c.year == year:
                classOfSchool.append(c)
                break
    
    marks = zip(students, classOfSchool, avgMarks1, avgMarks2)
    context = {
        'marks': marks,
        'marksFilter': marksFilter
    }
    return render(request, 'admin_template/traCuu.html', context=context)


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
                messages.success(request, "Cập nhật thành công")
                return redirect(reverse('bangDiem'))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Hãy điều đầy đủ vào ô thông tin !!!")
    else:
        return render(request, "admin_template/capNhatDiem.html", context)



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
    reports = Semester_Report().report_to_show(request.user.username, lop, hocKy, nienKhoa)
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
    age = Age.objects.all()
    context = {'age': age}
    return render(request, 'admin_template/quanLiTuoi.html', context=context)


def capNhatTuoi(request, age_id):
    age = get_object_or_404(Age, id=age_id)
    form = ageForm(request.POST or None, instance=age)
    context = {
        'form': form,
        'subject_id': age_id,
        'page_title': 'capNhatTuoi'
    }
    if request.method == 'POST':
        if form.is_valid():
            year = form.cleaned_data.get('year')
            max_age = form.cleaned_data.get('max_age')
            min_age = form.cleaned_data.get('min_age')
            try:
                Year = Age.objects.get(id=age.id)
                Year.year = year
                Year.max_age = max_age
                Year.min_age = min_age
                Year.save()
                messages.success(request, "Cập nhật thành công")
                return redirect(reverse('quanLiTuoi'))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Hãy điều đầy đủ vào ô thông tin !!!")
    else:
        return render(request, "admin_template/capNhatTuoi.html", context)


def xoaTuoi(request, age_id):
    age = get_object_or_404(Age, id=age_id)
    age.delete()
    messages.success(request, "Age deleted successfully!")
    return redirect(reverse('quanLiTuoi'))


def themTuoi(request):
    form = ageForm(request.POST or None)
    context = {
        'form': form,
        'page_title': 'themTuoi'
    }
    if request.method == 'POST':
        if form.is_valid():
            year = form.cleaned_data.get('year')
            max_age = form.cleaned_data.get('max_age')
            min_age = form.cleaned_data.get('min_age')
            try:
                Year = Age()
                Year.year = year
                Year.max_age = max_age
                Year.min_age = min_age
                Year.save()
                messages.success(request, "Thêm thành công")
                return redirect(reverse('quanLiTuoi'))
            except:
                messages.error(request, "Không thể thêm")
        else:
            messages.error(request, "Lỗi định dạng")
    return render(request, 'admin_template/themTuoi.html', context)


def quanLiLop(request):
    classes = ClassOfSchool.objects.all()
    yearFilter = YearFilter(request.GET, queryset=classes)
    classes = yearFilter.qs
    context = {
        'classes': classes,
        'yearFilter': yearFilter
    }
    return render(request, 'admin_template/quanLiLop.html', context=context)


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
                messages.success(request, "Cập nhật thành công")
                return redirect(reverse('quanLiLop'))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Hãy điều đầy đủ vào ô thông tin !!!")
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
                messages.success(request, "Thêm thành công")
                return redirect(reverse('quanLiLop'))
            except:
                messages.error(request, "Không thể thêm")
        else:
            messages.error(request, "Lỗi định dạng")
    return render(request, 'admin_template/themLop.html', context)


def quanLiMon(request):
    subjects = Subject.objects.all()
    subjectWithYearFilter = SubjectWithYearFilter(request.GET, queryset=subjects)
    subjects = subjectWithYearFilter.qs
    context = {
        'subjects': subjects,
        'subjectWithYearFilter': subjectWithYearFilter,
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
            subjectId = form.cleaned_data.get('SubjectID')
            name = form.cleaned_data.get('name')
            approved_mark = form.cleaned_data.get('approved_mark')
            try:
                subject = Subject.objects.get(id=subject.id)
                subject.SubjectID = subjectId
                subject.name = name
                subject.approved_mark = approved_mark
                subject.save()
                messages.success(request, "Cập nhật thành công")
                return redirect(reverse('quanLiMon'))
            except Exception as e:
                messages.error(request, "Could Not Update " + str(e))
        else:
            messages.error(request, "Hãy điều đầy đủ vào ô thông tin !!!")
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
            year = form.cleaned_data.get('year')
            try:
                subject = Subject()
                subject.SubjectID = SubjectID
                subject.name = name
                subject.approved_mark = approved_mark
                subject.year = Age.objects.get(year = year)
                subject.save()
                # thêm điểm vào tất cả học sinh có trong hệ thống
                students = Student.objects.all()
                for student in students:
                    for semester_mark in range(1, semester + 1):
                        mark = Mark()
                        mark.student = student
                        mark.subject = subject
                        mark.semester_mark = semester_mark
                        mark.markFifteen = 0
                        mark.markOne = 0
                        mark.markFinal = 0
                        mark.save()
                messages.success(request, "Thêm thành công")
                return redirect(reverse('quanLiMon'))
            except:
                messages.error(request, "không thể thêm")
        else:
            messages.error(request, "Lỗi định dạng")
    return render(request, 'admin_template/themMon.html', context)



def dsTaiKhoanHS(request):
    accountsStudent = Student.objects.all()
    formatDate = [a.user.dateOfBirth.strftime("%d-%m-%y") for a in accountsStudent]
    accounts = zip(accountsStudent,formatDate)
    context = {
            'accounts': accounts,
        }
    return render(request, 'admin_template/dsTaiKhoanHS.html', context=context)

def capNhatTKHS(request,account_id):
    account = get_object_or_404(Student, id=account_id)
    user = get_object_or_404(CustomUser, id=account.user.id)
    form = updateCustomUserForm(request.POST or None, instance=user)
    context = {
        'form': form,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            sex = form.cleaned_data.get('sex')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            try:
                account = Student.objects.get(id=account.id)
                user = CustomUser.objects.get(id = account.user.id)
                user.username = username
                user.name = name
                user.dateOfBirth = dateOfBirth
                user.sex = sex
                user.email = email
                user.phone = phone
                user.address = address
                user.save()
                messages.success(request, "Cập nhật thành công")
                return redirect(to='dsTaiKhoanHS')
            except:
                messages.error(request, "Không thể Không thể cập nhật")
        else:
            messages.error(request, "Dữ liệu không phù hợp")
    else:
        return render(request, "admin_template/capNhatHS.html", context)

def xoaTKHS(request,account_id):
    account = get_object_or_404(Student, id=account_id)
    account.delete()
    messages.success(request, "Xóa thành công !")
    return redirect(reverse('dsTaiKhoanHS'))

def dsTaiKhoanGV(request):
    accountsTeacher = Teacher.objects.all()
    formatDate = [a.user.dateOfBirth.strftime("%d-%m-%y") for a in accountsTeacher]
    classes = []
    for a in accountsTeacher:
        classes.append([c.classId for c in a.classOfSchool.all()])

    accounts = zip(accountsTeacher,formatDate, classes)
    context = {
            'accounts': accounts,
        }
    return render(request, 'admin_template/dsTaiKhoanGV.html', context=context)


def capNhatTKGV(request,account_id):
    account = get_object_or_404(Teacher, id=account_id)
    user = get_object_or_404(CustomUser, id=account.user.id)
    form = updateCustomUserForm(request.POST or None, instance=user)
    formTeacher = ClassTeacherForm(request.POST or None, instance=account)
    context = {
        'form': form,
        'formTeacher': formTeacher,
    }
    if request.method == 'POST':
        print(form.is_valid(),formTeacher.is_valid())
        if form.is_valid() and formTeacher.is_valid():
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            sex = form.cleaned_data.get('sex')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            subject = formTeacher.cleaned_data.get('subject')
            classOfSchool = formTeacher.cleaned_data.get('classOfSchool')
            try:
                account = Teacher.objects.get(id=account.id)
                user = CustomUser.objects.get(id = account.user.id)
                user.username = username
                user.name = name
                user.dateOfBirth = dateOfBirth
                user.sex = sex
                user.email = email
                user.phone = phone
                user.address = address
                user.save()
                if subject:
                    account.subject = subject
                account.save()
                for c  in classOfSchool:
                    account.classOfSchool.add(c)
                account.save()
                messages.success(request, "Cập nhật thành công")
                return redirect(to='dsTaiKhoanGV')
            except:
                messages.error(request, "Không thể Không thể cập nhật")
        else:
            messages.error(request, "Dữ liệu không phù hợp")
    else:
        return render(request, "admin_template/capNhatGV.html", context)

def xoaTKGV(request,account_id):
    account = get_object_or_404(Teacher, id=account_id)
    account.delete()
    messages.success(request, "Xóa thành công !")
    return redirect(reverse('dsTaiKhoanGV'))

def dsTaiKhoanAdmin(request):
    accountsAdmin = Admin.objects.all()
    formatDate = [a.user.dateOfBirth.strftime("%d-%m-%y") for a in accountsAdmin]
    accounts = zip(accountsAdmin,formatDate)
    context = {
            'accounts': accounts,
        }
    return render(request, 'admin_template/dsTaiKhoanAdmin.html', context=context)

def capNhatTKAdmin(request,account_id):
    account = get_object_or_404(Admin, id=account_id)
    user = get_object_or_404(CustomUser, id=account.user.id)
    form = updateCustomUserForm(request.POST or None, instance=user)
    context = {
        'form': form,
        'account_id': account_id,
    }
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name')
            dateOfBirth = form.cleaned_data.get('dateOfBirth')
            sex = form.cleaned_data.get('sex')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            address = form.cleaned_data.get('address')
            try:
                account = Admin.objects.get(id=account.id)
                user = CustomUser.objects.get(id = account.user.id)
                user.username = username
                user.name = name
                user.dateOfBirth = dateOfBirth
                user.sex = sex
                user.email = email
                user.phone = phone
                user.address = address
                user.save()
                messages.success(request, "Cập nhật thành công")
                return redirect(to='dsTaiKhoanAdmin')
            except:
                messages.error(request, "Không thể Không thể cập nhật")
        else:
            messages.error(request, "Dữ liệu không phù hợp")
    else:
        return render(request, "admin_template/capNhatAdmin.html", context)


def xoaTKAdmin(request,account_id):
    account = get_object_or_404(Admin, id=account_id)
    account.delete()
    messages.success(request, "Xóa thành công !")
    return redirect(reverse('dsTaiKhoanAdmin'))



# Teacher


# Student

def student_bangDiem(request):
    student = get_object_or_404(Student, user=request.user)
    if request.method != 'POST':
        classOfSchool = get_object_or_404(ClassOfSchool, classId=student.classOfSchool.classId)

        context = {
            # 'subjects': Subject.objects.filter(course=course),
            # 'page_title': 'View Attendance'
        }
        return render(request, 'admin_template/bangDiem.html', context)