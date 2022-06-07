from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *
from django.contrib.auth.models import Group
# @receiver(post_save,sender=User)
def createStudent(sender,instance,created, **kwargs):
    if created:
        group = Group.objects.get(name='student')
        instance.groups.add(group)

        Student.objects.create(
            user = instance,
            StudentID = instance.username
        )
        print('student created')

post_save.connect(createStudent,sender=User)
# @receiver(post_save,sender=User)
# def updateStudent(sender,instance,created, **kwargs):
#     if not created:
#         instance.student.save()