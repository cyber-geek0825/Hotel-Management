# Generated by Django 5.0.4 on 2024-05-08 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_users_rename_availability_hotels_base_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_phone', models.CharField(max_length=250)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('user_hotel', models.CharField(max_length=250)),
                ('special_request', models.TextField(null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_address',
            new_name='user_first_name',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='user_city',
            new_name='user_last_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='users',
            name='check_out',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_country',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_name',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_state',
        ),
        migrations.RemoveField(
            model_name='users',
            name='user_zip',
        ),
        migrations.AddField(
            model_name='users',
            name='title',
            field=models.CharField(default=None, max_length=5),
            preserve_default=False,
        ),
    ]