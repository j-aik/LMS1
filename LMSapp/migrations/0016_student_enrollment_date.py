# Generated by Django 5.0.4 on 2025-03-13 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0015_announcement'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='enrollment_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
