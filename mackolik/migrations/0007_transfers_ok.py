# Generated by Django 4.2.5 on 2023-10-02 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mackolik', '0006_remove_transfers_ok'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfers',
            name='ok',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oynadıgı_kulup', to='mackolik.club'),
        ),
    ]
