# Generated by Django 2.2.13 on 2022-10-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0022_auto_20221018_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us_detail',
            name='contact_number2',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]