# Generated by Django 4.0.3 on 2022-06-08 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentMan', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='year',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='studentMan.age'),
            preserve_default=False,
        ),
    ]
