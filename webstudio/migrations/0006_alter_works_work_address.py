# Generated by Django 3.2.4 on 2021-06-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstudio', '0005_auto_20210613_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='work_address',
            field=models.CharField(default='https://', max_length=300, null=True),
        ),
    ]
