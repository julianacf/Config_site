# Generated by Django 3.0.8 on 2020-08-19 17:33

from django.db import migrations, models
import macaddress.fields


class Migration(migrations.Migration):

    dependencies = [
        ('config_site', '0006_status_device'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='config_device',
            name='mac_adress',
        ),
        migrations.AddField(
            model_name='status_device',
            name='mac_adress',
            field=macaddress.fields.MACAddressField(blank=True, integer=True, null=True),
        ),
        migrations.AddField(
            model_name='status_device',
            name='serial_number',
            field=models.CharField(default=11111, max_length=20),
            preserve_default=False,
        ),
    ]
