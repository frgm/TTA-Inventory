# Generated by Django 2.0.2 on 2018-03-16 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_auto_20180316_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='ID_Loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Locations'),
        ),
        migrations.AlterField(
            model_name='distribution',
            name='ID_Prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Products'),
        ),
    ]
