# Generated by Django 5.1.3 on 2024-12-12 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_delete_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='slug',
        ),
    ]
