# Generated by Django 5.0 on 2024-01-27 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapi', '0003_remove_particularcourse_course_use_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inquerry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('mobile', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
            ],
        ),
    ]