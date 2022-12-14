# Generated by Django 2.2.13 on 2022-10-18 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0014_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='our_course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.TextField(blank=True, max_length=40, null=True)),
                ('course_description', models.TextField(blank=True, max_length=250, null=True)),
                ('course_logo', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
