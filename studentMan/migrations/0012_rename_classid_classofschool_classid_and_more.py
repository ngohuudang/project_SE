# Generated by Django 4.0.3 on 2022-05-26 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentMan', '0011_rename_subjectid_mark_mark_subject_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classofschool',
            old_name='ClassId',
            new_name='classId',
        ),
        migrations.RenameField(
            model_name='mark',
            old_name='Subject',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='ClassOfSchool',
            new_name='classOfSchool',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='ClassOfSchool',
            new_name='classOfSchool',
        ),
    ]
