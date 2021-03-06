# Generated by Django 3.0.8 on 2020-07-22 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('op_mode', models.CharField(choices=[('0', 'Gateway'), ('1', 'Roteador')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=8)),
            ],
        ),
    ]
