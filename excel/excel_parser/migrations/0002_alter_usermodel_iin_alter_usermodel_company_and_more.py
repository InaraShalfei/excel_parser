# Generated by Django 4.2 on 2023-04-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='IIN',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='company',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='company_branch',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='document_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='planned_finish_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='planned_start_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='real_finish_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='real_start_time',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]