# Generated by Django 2.0.2 on 2018-03-22 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20180305_2133'),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default=0)),
                ('Date', models.DateTimeField(verbose_name='')),
            ],
        ),
        migrations.RemoveField(
            model_name='locations',
            name='Coordinates',
        ),
        migrations.RemoveField(
            model_name='requisition',
            name='ID_Emp',
        ),
        migrations.AddField(
            model_name='employees',
            name='Name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='employees',
            name='Password',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='locations',
            name='Latitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='locations',
            name='Longitude',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employees',
            name='Role',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='locations',
            name='Address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='locations',
            name='Name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='products',
            name='Name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='report',
            name='ID_Emp',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Employees'),
        ),
        migrations.AddField(
            model_name='report',
            name='ID_Loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Locations'),
        ),
        migrations.AddField(
            model_name='report',
            name='ID_Prod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Products'),
        ),
    ]