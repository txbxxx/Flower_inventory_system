# Generated by Django 4.2.8 on 2023-12-21 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flowers_base', '0004_alter_flower_data_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flower_data',
            name='classi',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='flowers_base.flower_class', to_field='class_name'),
        ),
    ]
