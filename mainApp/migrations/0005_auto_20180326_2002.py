# Generated by Django 2.0.2 on 2018-03-26 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0004_employees_id_loc'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictedRequisition',
            fields=[
                ('Quantity', models.IntegerField(default=0)),
                ('Date', models.DateTimeField(primary_key=True, serialize=False, verbose_name='')),
            ],
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='ID_Prod',
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='id',
        ),
        migrations.AlterField(
            model_name='locations',
            name='Latitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='locations',
            name='Longitude',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='products',
            name='Material',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='requisition',
            name='Date',
            field=models.DateTimeField(primary_key=True, serialize=False, verbose_name=''),
        ),
        migrations.AddField(
            model_name='predictedrequisition',
            name='ID_Loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Locations'),
        ),
    ]
