# Generated by Django 4.2.2 on 2024-05-16 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pixelapp', '0005_alter_mymodel_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatsdata',
            name='image_base64',
            field=models.TextField(default='none'),
        ),
    ]