# Generated by Django 5.2 on 2025-05-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casalivingapp', '0004_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='location',
            field=models.TextField(),
        ),
    ]
