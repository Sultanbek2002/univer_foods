# Generated by Django 4.2 on 2023-04-28 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientuser',
            name='passport_photo_down',
            field=models.ImageField(null=True, upload_to='media/passport/down/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='clientuser',
            name='passport_photo_up',
            field=models.ImageField(null=True, upload_to='media/passport/%Y/%m/%d'),
        ),
        migrations.AddField(
            model_name='clientuser',
            name='status_user',
            field=models.CharField(default='viewer', max_length=40, null=True),
        ),
    ]
