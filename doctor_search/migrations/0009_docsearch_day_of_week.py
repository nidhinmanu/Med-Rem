# Generated by Django 4.0.5 on 2022-11-05 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor_search', '0008_remove_docsearch_day_of_week'),
    ]

    operations = [
        migrations.AddField(
            model_name='docsearch',
            name='day_of_week',
            field=models.ManyToManyField(to='doctor_search.dayofweek'),
        ),
    ]
