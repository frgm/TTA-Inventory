# Generated by Django 2.0.2 on 2018-03-06 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employees',
            name='id',
        ),
        migrations.RemoveField(
            model_name='locations',
            name='id',
        ),
        migrations.RemoveField(
            model_name='products',
            name='id',
        ),
        migrations.AlterField(
            model_name='employees',
            name='ID_Emp',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='locations',
            name='ID_Loc',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='products',
            name='ID_Prod',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
