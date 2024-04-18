# Generated by Django 5.0.4 on 2024-04-18 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField()),
                ('status', models.IntegerField(choices=[(0, 'active'), (1, 'inactive')], default=0)),
                ('role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_app.role')),
            ],
        ),
    ]
