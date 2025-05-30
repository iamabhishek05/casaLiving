# Generated by Django 5.2 on 2025-05-04 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('casalivingapp', '0002_amenitytag_room_amenities_houseamenity'),
    ]

    operations = [
        migrations.CreateModel(
            name='HouseImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='houses/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houseImage', to='casalivingapp.house')),
            ],
        ),
    ]
