# Generated by Django 5.0.1 on 2024-03-10 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RideReady_app', '0005_profile1'),
    ]

    operations = [
        migrations.CreateModel(
            name='profile2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('zipCode', models.CharField(max_length=100)),
                ('bankName', models.CharField(max_length=100)),
                ('accountNumber', models.CharField(max_length=100)),
                ('ifscCode', models.CharField(max_length=100)),
            ],
        ),
    ]
