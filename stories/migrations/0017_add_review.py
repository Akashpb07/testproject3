# Generated by Django 2.2.13 on 2022-10-18 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0016_auto_20221018_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=40, null=True)),
                ('message', models.TextField()),
            ],
        ),
    ]