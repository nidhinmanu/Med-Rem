# Generated by Django 4.0.5 on 2022-11-04 20:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='medicinerecord',
            options={'ordering': ['medicine_name']},
        ),
    ]
