# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-05-03 20:06
from __future__ import unicode_literals

from django.db import migrations, models
import plugins.fields


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plugin',
            name='max_cpu_limit',
            field=plugins.fields.CPUField(blank=True, default=2147483647, null=True),
        ),
        migrations.AddField(
            model_name='plugin',
            name='max_gpu_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plugin',
            name='max_memory_limit',
            field=plugins.fields.MemoryField(blank=True, default=2147483647, null=True),
        ),
        migrations.AddField(
            model_name='plugin',
            name='max_number_of_workers',
            field=models.IntegerField(blank=True, default=2147483647, null=True),
        ),
        migrations.AddField(
            model_name='plugin',
            name='min_cpu_limit',
            field=plugins.fields.CPUField(blank=True, default=1000, null=True),
        ),
        migrations.AddField(
            model_name='plugin',
            name='min_gpu_limit',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='plugin',
            name='min_memory_limit',
            field=plugins.fields.MemoryField(blank=True, default=200, null=True),
        ),
        migrations.AddField(
            model_name='plugin',
            name='min_number_of_workers',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='pluginparameter',
            name='action',
            field=models.CharField(default='store', max_length=20),
        ),
        migrations.AddField(
            model_name='pluginparameter',
            name='flag',
            field=models.CharField(default='', max_length=52),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pluginparameter',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]