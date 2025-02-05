# Generated by Django 4.2.1 on 2023-06-29 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0004_moviedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_id', models.IntegerField()),
                ('purchase_date', models.DateField()),
                ('movie_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.moviedata')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.userdata')),
            ],
        ),
    ]
