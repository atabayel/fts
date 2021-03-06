# Generated by Django 2.0.5 on 2018-05-03 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=50)),
                ('surname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=120)),
                ('reg_date', models.CharField(max_length=20)),
                ('rating', models.CharField(default='0', max_length=20)),
                ('refused_orders', models.CharField(default='0', max_length=20)),
                ('completed_orders', models.CharField(default='0', max_length=20)),
            ],
        ),
    ]
