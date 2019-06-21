# Generated by Django 2.2.2 on 2019-06-21 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('booking_type', models.CharField(choices=[('dog_walk', 'Dog Walk'), ('housekeeping', 'Housekeeping')], max_length=30)),
                ('booking_date', models.DateField(db_index=True)),
                ('booking_time', models.TimeField(db_index=True)),
            ],
            options={
                'ordering': ['booking_date', 'booking_time'],
            },
        ),
    ]
