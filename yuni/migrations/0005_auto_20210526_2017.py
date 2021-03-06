# Generated by Django 3.2 on 2021-05-26 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yuni', '0004_auto_20210524_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventory',
            name='branchId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventory_code', to='yuni.branch'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='customerId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='inventory_code', to='yuni.customer'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='mrp',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='customerId',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uid', to='yuni.customer'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='additionalParam',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='additionalParam',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='additionalParam',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='lastPurchasedStore',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uid', to='yuni.branch'),
        ),
    ]
