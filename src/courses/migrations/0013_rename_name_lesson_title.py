# Generated by Django 5.1.7 on 2025-04-03 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0012_lesson_public_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='name',
            new_name='title',
        ),
    ]
