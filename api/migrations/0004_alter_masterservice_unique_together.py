# Generated by Django 5.0.3 on 2024-03-14 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_masterservice_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='masterservice',
            unique_together=set(),
        ),
    ]
