# Generated by Django 3.1.7 on 2021-02-21 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_auto_20210221_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
    ]
