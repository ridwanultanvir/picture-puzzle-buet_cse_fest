# Generated by Django 4.0.5 on 2022-06-23 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_remove_participant_batch_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='batch',
            field=models.IntegerField(default=0),
        ),
    ]
