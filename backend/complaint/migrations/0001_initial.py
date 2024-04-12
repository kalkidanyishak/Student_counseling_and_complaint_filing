<<<<<<< HEAD
# Generated by Django 5.0.4 on 2024-04-11 18:37
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
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(choices=[('grade_issue', 'Grade Issue'), ('harassment_teacher', 'Harassment - Teacher'), ('harassment_student', 'Harassment - Student'), ('bullied', 'Bullied'), ('lounge', 'Lounge'), ('other', 'Other')], max_length=50, verbose_name='Tags')),
                ('body', models.TextField(verbose_name='Body')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('tag', 'body')},
            },
        ),
    ]
