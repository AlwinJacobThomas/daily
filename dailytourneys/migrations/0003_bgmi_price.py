# Generated by Django 3.2.13 on 2022-07-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailytourneys', '0002_remove_bgmi_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bgmi',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]