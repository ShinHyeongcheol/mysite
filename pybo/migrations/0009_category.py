# Generated by Django 3.2.13 on 2022-05-29 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0008_question_mainphoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('has_answer', models.BooleanField(default=True)),
            ],
        ),
    ]