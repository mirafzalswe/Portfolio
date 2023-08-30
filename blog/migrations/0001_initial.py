# Generated by Django 4.2.3 on 2023-08-24 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='blog_image')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=400)),
            ],
        ),
    ]