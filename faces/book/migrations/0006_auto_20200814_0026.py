# Generated by Django 3.0.6 on 2020-08-14 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20200813_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mybooksread',
            name='authors',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mybooksread',
            name='book_title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='mybooksread',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
