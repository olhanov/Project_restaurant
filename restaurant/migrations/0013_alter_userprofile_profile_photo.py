# Generated by Django 5.1.2 on 2024-11-10 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0012_alter_testimonial_profession_usercomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='user_profiles/'),
        ),
    ]
