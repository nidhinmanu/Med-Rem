# Generated by Django 4.0.5 on 2022-11-06 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_pat', '0004_alter_patientrec_medicine_rec'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientGender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='patientrec',
            name='gender',
        ),
    ]
