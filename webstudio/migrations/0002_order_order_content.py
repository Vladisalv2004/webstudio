# Generated by Django 3.2.4 on 2021-06-27 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstudio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_content',
            field=models.TextField(null=True),
        ),
    ]