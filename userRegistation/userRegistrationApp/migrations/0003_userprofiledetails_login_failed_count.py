# Generated by Django 3.1.3 on 2020-12-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userRegistrationApp', '0002_userprofiledetails_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiledetails',
            name='login_failed_count',
            field=models.IntegerField(default=0),
        ),
    ]
