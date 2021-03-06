# Generated by Django 3.2.7 on 2021-09-28 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='name of product', max_length=120)),
                ('image', models.ImageField(default='no_picture.png', upload_to='products')),
                ('price', models.FloatField(help_text='In Indian Rupees ₹')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date when created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='Date when updated')),
            ],
        ),
    ]
