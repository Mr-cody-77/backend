# Generated by Django 5.0.2 on 2025-01-13 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuditionForm', '0003_alter_auditiondata_domain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auditiondata',
            name='desc',
        ),
    ]
