# Generated by Django 5.0.4 on 2025-03-06 16:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_staff_member',
        ),
    ]
