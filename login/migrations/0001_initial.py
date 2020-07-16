# Generated by Django 3.0.7 on 2020-07-04 02:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gst_field.modelfields
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pan_card', gst_field.modelfields.PANField(max_length=10)),
                ('mobile_number', phone_field.models.PhoneField(help_text='Contact phone number', max_length=31)),
            ],
        ),
        migrations.CreateModel(
            name='User_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='login.User_details')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
