# Generated by Django 4.2.4 on 2023-09-09 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('emro_boarding_house', '0004_maintenance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=255)),
                ('rent', models.CharField(max_length=255)),
                ('electricity', models.CharField(max_length=255)),
                ('water', models.CharField(max_length=255)),
                ('due_date', models.DateField()),
                ('status', models.CharField(max_length=255)),
                ('boarder_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emro_boarding_house.boarder')),
            ],
        ),
    ]
