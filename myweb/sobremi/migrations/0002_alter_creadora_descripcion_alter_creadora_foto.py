# Generated by Django 4.0.2 on 2022-02-16 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sobremi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creadora',
            name='descripcion',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='creadora',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='sobremi'),
        ),
    ]
