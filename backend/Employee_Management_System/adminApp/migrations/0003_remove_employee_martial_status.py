# Generated by Django 4.1.3 on 2022-12-12 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminApp', '0002_employee_marital_status_alter_employee_blood_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='martial_Status',
        ),
    ]
