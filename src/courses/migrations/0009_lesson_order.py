# Generated by Django 5.1.7 on 2025-04-03 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_course_created_at_course_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
