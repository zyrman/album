# Generated by Django 3.1.7 on 2021-02-21 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_photo_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
