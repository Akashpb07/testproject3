# Generated by Django 2.2.13 on 2022-10-18 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0015_our_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='institute_deatil',
            name='address',
        ),
        migrations.RemoveField(
            model_name='institute_deatil',
            name='city',
        ),
        migrations.RemoveField(
            model_name='institute_deatil',
            name='email',
        ),
        migrations.RemoveField(
            model_name='institute_deatil',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='institute_deatil',
            name='state',
        ),
        migrations.RemoveField(
            model_name='institute_deatil',
            name='zip_code',
        ),
    ]