# Generated by Django 5.0.1 on 2024-03-19 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RideReady_app', '0008_alter_profile_email_alter_profile1_dob_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fathername', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('id_number', models.CharField(max_length=100)),
                ('account_number', models.CharField(max_length=100)),
                ('bank_name', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('ex_showroom_price', models.CharField(max_length=100)),
                ('loan_amount', models.CharField(max_length=100)),
                ('initial_amount', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='profile1',
        ),
        migrations.DeleteModel(
            name='profile2',
        ),
        migrations.DeleteModel(
            name='profile3',
        ),
    ]
