# Generated by Django 5.0.4 on 2025-03-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0011_alter_staff_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='class_assigned',
        ),
        migrations.AddField(
            model_name='staff',
            name='class_assigned',
            field=models.ManyToManyField(blank=True, null=True, to='LMSapp.classst'),
        ),
    ]
