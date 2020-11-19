# Generated by Django 3.1.2 on 2020-11-19 08:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('idNumber', models.CharField(max_length=20)),
                ('dateOfBirth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Virus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('commonName', models.CharField(max_length=20)),
                ('maxInfectiousPeriod', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CaseRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfConfirm', models.DateField()),
                ('localOrImported', models.CharField(max_length=20)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewCases.patient')),
                ('virus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewCases.virus')),
            ],
        ),
    ]
