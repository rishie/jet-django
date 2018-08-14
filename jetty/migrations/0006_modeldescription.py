# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-14 07:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('jetty', '0005_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=255, verbose_name='app_label')),
                ('model', models.CharField(blank=True, default='', max_length=255, verbose_name='model')),
                ('params', models.TextField(blank=True, default='', verbose_name='params')),
                ('date_add', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date added')),
            ],
            options={
                'verbose_name': 'model description',
                'verbose_name_plural': 'model descriptions',
            },
        ),
    ]