# Generated by Django 2.2.13 on 2022-10-18 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0017_add_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField()),
                ('email', models.TextField()),
                ('contact_number1', models.CharField(max_length=12)),
            ],
        ),
    ]
