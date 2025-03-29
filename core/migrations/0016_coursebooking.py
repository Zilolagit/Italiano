# Generated by Django 5.1.7 on 2025-03-29 20:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_course_options_remove_course_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='core.course')),
            ],
        ),
    ]
