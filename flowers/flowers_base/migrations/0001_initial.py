# Generated by Django 4.2.8 on 2023-12-19 01:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin_data',
            fields=[
                ('admin_id', models.IntegerField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=30)),
                ('telephone', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='flower_class',
            fields=[
                ('class_id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='flower_data',
            fields=[
                ('flower_id', models.IntegerField(primary_key=True, serialize=False)),
                ('flower_name', models.CharField(max_length=20)),
                ('price', models.IntegerField(null=True)),
                ('num', models.IntegerField()),
                ('classi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers_base.flower_class')),
            ],
        ),
    ]
