# Generated by Django 2.1.4 on 2019-02-11 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plugins', '0004_auto_20180802_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='DefaultBoolParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='DefaultFloatParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='DefaultIntParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='DefaultPathParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DefaultStringParameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(blank=True, max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='pluginparameter',
            name='default',
        ),
        migrations.AddField(
            model_name='defaultstringparameter',
            name='plugin_param',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='string_default', to='plugins.PluginParameter'),
        ),
        migrations.AddField(
            model_name='defaultpathparameter',
            name='plugin_param',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='path_default', to='plugins.PluginParameter'),
        ),
        migrations.AddField(
            model_name='defaultintparameter',
            name='plugin_param',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='integer_default', to='plugins.PluginParameter'),
        ),
        migrations.AddField(
            model_name='defaultfloatparameter',
            name='plugin_param',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='float_default', to='plugins.PluginParameter'),
        ),
        migrations.AddField(
            model_name='defaultboolparameter',
            name='plugin_param',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='boolean_default', to='plugins.PluginParameter'),
        ),
    ]
