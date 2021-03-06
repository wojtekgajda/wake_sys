# Generated by Django 2.2.13 on 2020-07-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wake_sys', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='duration',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4')]),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='hour',
            field=models.IntegerField(choices=[(10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17'), (18, '18'), (19, '19')]),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='start_slot',
            field=models.IntegerField(choices=[(0, '00'), (15, '15'), (30, '30'), (45, '45')]),
        ),
    ]
