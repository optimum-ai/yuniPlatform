# Generated by Django 3.2 on 2021-05-31 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yuni', '0008_auto_20210527_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='createdon',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='date_of_birth',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='member',
            name='lastmodifiedon',
            field=models.DateTimeField(),
        ),
    ]