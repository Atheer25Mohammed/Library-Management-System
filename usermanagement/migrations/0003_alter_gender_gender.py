# Generated by Django 5.0 on 2023-12-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0002_alter_userprofile_city_alter_userprofile_faculty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.BooleanField(max_length=1),
        ),
    ]