# Generated by Django 3.1.8 on 2023-07-12 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_lead_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='experience',
            field=models.CharField(choices=[('yes', 'Yes'), ('no', 'No')], max_length=3),
        ),
    ]
