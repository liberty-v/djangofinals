# Generated by Django 4.2.4 on 2023-09-05 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emro_boarding_house', '0002_boarder_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roomt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_num', models.CharField(max_length=255)),
                ('monthly_rent', models.CharField(max_length=255)),
                ('availability', models.CharField(max_length=255)),
            ],
        ),
    ]
