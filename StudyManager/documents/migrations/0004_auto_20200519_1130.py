# Generated by Django 3.0.6 on 2020-05-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_isd_document_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='isd_document',
            name='course',
            field=models.CharField(choices=[('ISD', 'Information System Development'), ('EAM', 'Enterprise Architecture Management'), ('BLA', 'blakjsdflk')], default=0, max_length=3),
            preserve_default=False,
        ),
    ]