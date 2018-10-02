# Generated by Django 2.1.1 on 2018-10-01 22:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Giatroi',
            fields=[
                ('fullname', models.CharField(max_length=50)),
                ('amka', models.DecimalField(decimal_places=0, max_digits=11, primary_key=True, serialize=False)),
                ('eidikotita', models.CharField(max_length=50)),
                ('til', models.DecimalField(decimal_places=0, max_digits=10)),
                ('perioxi', models.CharField(max_length=50)),
                ('radevous', models.TextField(max_length=3001)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('radevous', models.TextField(max_length=3001)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Radevou',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=46)),
                ('description', models.TextField(default='', max_length=3001)),
                ('eidi', models.CharField(default='', max_length=80)),
                ('peri', models.CharField(default='', max_length=80)),
                ('fu', models.CharField(default='', max_length=50)),
                ('radevou', models.TextField(default='', max_length=3001)),
                ('til', models.DecimalField(decimal_places=0, max_digits=10)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
