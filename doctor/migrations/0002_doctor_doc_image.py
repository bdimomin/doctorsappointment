# Generated by Django 4.2.3 on 2023-07-23 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='doc_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/doctor/'),
        ),
    ]