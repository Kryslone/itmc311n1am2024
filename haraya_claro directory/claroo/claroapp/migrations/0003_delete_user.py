# Generated by Django 5.1 on 2024-10-06 22:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('claroapp', '0002_user_groups_user_is_active_user_is_staff_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
