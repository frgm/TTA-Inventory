# Generated by Django 2.0.2 on 2018-03-24 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_auto_20180322_2002'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='ID_Loc',
            field=models.IntegerField(default=0),
        ),
    ]
