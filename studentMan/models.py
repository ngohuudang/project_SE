from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import User


class Account(models.Model):
    username = models.CharField(max_length=30, null=False, unique=True)
    password = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.username


class Age(models.Model):
    year = models.CharField(max_length=200, null=False, unique=True)
    max_age = models.IntegerField()
    min_age = models.IntegerField()

    def __str__(self):
        return self.year


class ClassOfSchool(models.Model):
    ClassId = models.CharField(max_length=200, null=False, unique=False)
    max_number = models.IntegerField()
    year = models.ForeignKey(Age, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.ClassId


class Subject(models.Model):
    SubjectID = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=False, unique=True)
    approved_mark = models.FloatField()

    def __str__(self):
        return self.SubjectID


class Student(models.Model):
    SEX_CATELOGY = (
        ('nam', 'nam'),
        ('nu', 'nu')
    )
    StudentID = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    dateOfBirth = models.DateTimeField()
    sex = models.CharField(max_length=200, null=True, choices=SEX_CATELOGY)
    username = models.ForeignKey(Account, null=False, on_delete=models.CASCADE)
    year = models.ForeignKey(Age, null=False, on_delete=models.CASCADE)
    ClassOfSchool = models.ForeignKey(ClassOfSchool, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    SEX_CATELOGY = (
        ('nam', 'nam'),
        ('nu', 'nu')
    )
    TeacherID = models.CharField(max_length=200, null=False, unique=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    dateOfBirth = models.DateTimeField()
    sex = models.CharField(max_length=200, null=True, choices=SEX_CATELOGY)
    username = models.ForeignKey(Account, null=False, on_delete=models.CASCADE)
    year = models.ForeignKey(Age, null=False, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)
    ClassOfSchool = models.ForeignKey(ClassOfSchool, null=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Mark(models.Model):
    SEMESTER_CATELOGY = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3')
    )
    StudentID_mark = models.ForeignKey(Student, related_name='ID_mark', null=False, on_delete=models.CASCADE)
    year_mark = models.ForeignKey(Student, related_name='year_mark', null=False, on_delete=models.CASCADE)
    semester_mark = models.CharField(max_length=200, null=False, choices=SEMESTER_CATELOGY)
    SubjectID_mark = models.ForeignKey(Subject, null=False, on_delete=models.CASCADE)
    markFifteen = models.FloatField()
    markFinal = models.FloatField()
    markOne = models.FloatField()


