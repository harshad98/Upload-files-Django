# Generated by Django 2.1.4 on 2019-01-31 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prax', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='books/covers/'),
        ),
    ]
