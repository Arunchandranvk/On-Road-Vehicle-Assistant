# Generated by Django 5.0.2 on 2024-04-09 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_carrenterprofile_profile_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='static/images/profile/default.jpg', null=True, upload_to='userprofile'),
        ),
    ]
