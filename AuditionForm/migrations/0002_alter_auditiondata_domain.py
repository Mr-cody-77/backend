# Generated by Django 5.0.2 on 2024-12-31 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuditionForm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditiondata',
            name='domain',
            field=models.TextField(blank=True, null=True),
        ),
    ]
