# Generated by Django 5.0.4 on 2025-03-07 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LMSapp', '0004_customuser_is_admin_customuser_is_parent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
