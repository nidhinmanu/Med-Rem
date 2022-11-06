# Generated by Django 4.0.5 on 2022-11-05 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_search', '0002_speciality_alter_docsearch_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsearch',
            name='speciality',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='doctor_search.speciality'),
        ),
    ]