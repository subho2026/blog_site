# Generated by Django 4.2.5 on 2023-09-19 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_experience_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Experience',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
