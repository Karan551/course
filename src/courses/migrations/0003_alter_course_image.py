# Generated by Django 5.1.7 on 2025-04-01 14:31

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='image'),
        ),
    ]
