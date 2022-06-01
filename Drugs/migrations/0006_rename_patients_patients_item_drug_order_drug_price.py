# Generated by Django 4.0.2 on 2022-05-31 18:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Drugs', '0005_drug_order_appointment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patients',
            new_name='Patients_item',
        ),
        migrations.AddField(
            model_name='drug_order',
            name='Drug_price',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]