# Generated by Django 2.2.13 on 2022-10-18 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0012_auto_20221018_1409'),
    ]

    operations = [
        migrations.CreateModel(
            name='ourcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_name', models.TextField(max_length=20)),
                ('card_description', models.TextField()),
                ('card_icon', models.TextField()),
            ],
        ),
    ]