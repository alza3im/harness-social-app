# Generated by Django 4.2.2 on 2023-06-16 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usergeolocation'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergeolocation',
            name='country_code',
            field=models.CharField(max_length=2, null=True),
        ),
    ]