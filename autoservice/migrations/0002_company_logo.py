# Generated by Django 3.2.16 on 2023-09-16 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autoservice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(null=True, upload_to='logo_companys/', verbose_name='Логотип компании'),
        ),
    ]
