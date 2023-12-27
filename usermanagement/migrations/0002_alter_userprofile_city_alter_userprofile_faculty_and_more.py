# Generated by Django 5.0 on 2023-12-27 08:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usermanagement', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usermanagement.city'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='faculty',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usermanagement.faculty'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=models.SET(1), to='usermanagement.gender'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='semester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usermanagement.semester'),
        ),
    ]