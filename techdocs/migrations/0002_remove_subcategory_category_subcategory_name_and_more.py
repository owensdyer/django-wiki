# Generated by Django 5.0.6 on 2024-05-21 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('techdocs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subcategory',
            name='category',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='supercategory',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='technicaldoc',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
