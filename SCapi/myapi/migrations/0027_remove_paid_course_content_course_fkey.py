# Generated by Django 4.1.13 on 2024-03-26 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0026_paid_course_content_course_fkey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paid_course_content',
            name='Course_FKey',
        ),
    ]