# Generated by Django 4.0.5 on 2022-11-08 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_search', '0016_docsearch_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsearch',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='specialities', to='doctor_search.speciality'),
        ),
    ]
