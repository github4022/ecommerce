# Generated by Django 5.0.4 on 2024-05-17 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=None, upload_to='category/'),
        ),
    ]
