# Generated by Django 4.0.1 on 2022-01-31 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NTPC',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Finance', models.CharField(blank=True, max_length=300)),
                ('Monday', models.CharField(blank=True, max_length=1500)),
                ('Tuesday', models.CharField(blank=True, max_length=1500)),
                ('Wednesday', models.CharField(blank=True, max_length=1500)),
                ('Thursday', models.CharField(blank=True, max_length=1500)),
                ('Friday', models.CharField(blank=True, max_length=1500)),
            ],
        ),
    ]
