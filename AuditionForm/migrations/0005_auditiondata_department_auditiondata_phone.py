# Generated by Django 5.0.2 on 2025-01-13 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuditionForm', '0004_remove_auditiondata_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditiondata',
            name='department',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='auditiondata',
            name='phone',
            field=models.IntegerField(max_length=10, null=True),
        ),
    ]
