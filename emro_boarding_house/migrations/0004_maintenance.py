# Generated by Django 4.2.4 on 2023-09-06 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emro_boarding_house', '0003_roomt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_desc', models.CharField(max_length=500)),
                ('status', models.CharField(max_length=255)),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emro_boarding_house.roomt')),
            ],
        ),
    ]
