# Generated by Django 4.0.5 on 2022-11-06 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register_pat', '0005_patientgender_remove_patientrec_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientrec',
            name='gender',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='register_pat.patientgender'),
            preserve_default=False,
        ),
    ]
