# Generated by Django 4.1.4 on 2023-03-05 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_customuser_delete_city'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'blog'},
        ),
    ]
