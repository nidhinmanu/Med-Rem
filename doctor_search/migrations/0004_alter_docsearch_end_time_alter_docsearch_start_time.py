# Generated by Django 4.0.5 on 2022-11-05 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_search', '0003_alter_docsearch_speciality'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docsearch',
            name='end_time',
            field=models.ForeignKey(default='', on_delete=models.SET(''), related_name='+', to='doctor_search.availabletime'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='docsearch',
            name='start_time',
            field=models.ForeignKey(default='', on_delete=models.SET(''), related_name='+', to='doctor_search.availabletime'),
            preserve_default=False,
        ),
    ]
