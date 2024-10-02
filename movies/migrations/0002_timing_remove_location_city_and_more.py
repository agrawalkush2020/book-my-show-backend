# Generated by Django 5.1.1 on 2024-10-02 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='location',
            name='city',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='number_of_seats',
        ),
        migrations.AddField(
            model_name='movie',
            name='timings',
            field=models.ManyToManyField(related_name='timings', to='movies.timing'),
        ),
    ]
