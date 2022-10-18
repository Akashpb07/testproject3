# Generated by Django 2.2.13 on 2022-10-08 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='institute_deatils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('phone_number', models.CharField(max_length=12)),
                ('main_quote_line1', models.TextField()),
                ('main_quote_line2', models.TextField()),
                ('address', models.CharField(max_length=128, verbose_name='address')),
                ('city', models.CharField(default='Hoshiarpur', max_length=64, verbose_name='city')),
                ('state', models.CharField(default='PB', max_length=64, verbose_name='state')),
                ('zip_code', models.CharField(default='146001', max_length=5, verbose_name='zip code')),
            ],
        ),
    ]
