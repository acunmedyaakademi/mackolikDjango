# Generated by Django 4.2.5 on 2023-09-26 10:50

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mackolik', '0002_club_puan'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='slug',
            field=autoslug.fields.AutoSlugField(blank=True, editable=True, populate_from='name', unique=True),
        ),
    ]