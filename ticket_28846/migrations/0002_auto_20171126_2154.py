# Generated by Django 2.1.dev20171124082118 on 2017-11-26 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_28846', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bar',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
