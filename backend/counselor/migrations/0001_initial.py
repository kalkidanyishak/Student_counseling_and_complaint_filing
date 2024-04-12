<<<<<<< HEAD
# Generated by Django 5.0.4 on 2024-04-11 18:51
=======
# Generated by Django 5.0.4 on 2024-04-12 06:03
>>>>>>> 9c02e62f0d45c4c80ed4c7b15c00c54c32da012b

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CounselorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('gender', models.CharField(max_length=6)),
=======
                ('gender', models.CharField(max_length=7)),
>>>>>>> 9c02e62f0d45c4c80ed4c7b15c00c54c32da012b
                ('bio', models.TextField()),
                ('languages', models.TextField()),
                ('specialities', models.TextField()),
                ('years_of_experience', models.IntegerField(default=0)),
                ('verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_datetime', models.DateTimeField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('counselor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='counselor.counselorprofile')),
            ],
        ),
    ]
