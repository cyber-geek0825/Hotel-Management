# Generated by Django 5.0.4 on 2024-05-06 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_remove_hotels_room_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=250)),
                ('user_email', models.EmailField(max_length=250)),
                ('user_phone', models.CharField(max_length=250)),
                ('user_address', models.CharField(max_length=250)),
                ('user_city', models.CharField(max_length=250)),
                ('user_state', models.CharField(max_length=250)),
                ('user_zip', models.CharField(max_length=250)),
                ('user_country', models.CharField(max_length=250)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
            ],
        ),
        migrations.RenameField(
            model_name='hotels',
            old_name='availability',
            new_name='base_price',
        ),
        migrations.AddField(
            model_name='hotels',
            name='tax_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='hotels',
            name='total_price',
            field=models.IntegerField(null=True),
        ),
    ]
