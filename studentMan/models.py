from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User

class Age(models.Model):
    year = models.CharField(max_length=200, null=False, unique=True)
    max_age = models.IntegerField(null=False)
    min_age = models.IntegerField(null=False)
    def __str__(self):
        return self.year

class ClassOfSchool(models.Model):
    classId = models.CharField(max_length=200, null=False, unique=False)
    max_number = models.IntegerField(null=False)
    year = models.ForeignKey(Age, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.classId


class Subject(models.Model):
    SubjectID = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=False, unique=True)
    approved_mark = models.FloatField(null=False)

    def __str__(self):
        return self.SubjectID


class Student(models.Model):
    SEX_CATELOGY = (
        ('nam', 'nam'),
        ('nu', 'nu')
    )
    StudentID = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=200, null=True, choices=SEX_CATELOGY)
    dateOfBirth = models.DateTimeField()
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True,null=True)
    address = models.TextField(null=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    year = models.ForeignKey(Age, null=False, on_delete=models.CASCADE)
    classOfSchool = models.ForeignKey(ClassOfSchool, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    SEX_CATELOGY = (
        ('nam', 'nam'),
        ('nu', 'nữ')
    )
    TeacherID = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=True)
    sex = models.CharField(max_length=200, null=True, choices=SEX_CATELOGY)
    dateOfBirth = models.DateTimeField(blank = True, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True,null=True)
    address = models.TextField(null=True)
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    year = models.ForeignKey(Age, null=False, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)
    classOfSchool = models.ForeignKey(ClassOfSchool, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mark(models.Model):
    SEMESTER_CATEGORY = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    )
    student = models.ForeignKey(Student,null=True, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)
    semester_mark = models.CharField(max_length=200, null=False, choices=SEMESTER_CATEGORY)
    markFifteen = models.FloatField(null=True)
    markOne = models.FloatField(null=True)
    markFinal = models.FloatField(null=True)
    


