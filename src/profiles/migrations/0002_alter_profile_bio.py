# Generated by Django 3.2.7 on 2021-09-29 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Add about you..... Let People know about what kind of person you are!'),
        ),
    ]
