# Generated by Django 3.2.3 on 2021-09-27 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.CharField(blank=True, max_length=170, verbose_name='Уақыты'),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, upload_to='image'),
        ),
    ]
