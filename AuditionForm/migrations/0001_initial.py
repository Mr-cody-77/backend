# Generated by Django 5.0.2 on 2024-12-31 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditionData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('roll', models.CharField(max_length=10, null=True, unique=True)),
                ('domain', models.JSONField(blank=True, default=list, null=True)),
                ('desc', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
