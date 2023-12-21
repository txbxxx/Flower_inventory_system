# Generated by Django 4.2.8 on 2023-12-20 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flowers_transcaction', '0003_alter_inbound_flowers_alter_outbound_flowers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inbound',
            name='inbound_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='outbound',
            name='outbound_id',
            field=models.IntegerField(unique=True),
        ),
    ]
