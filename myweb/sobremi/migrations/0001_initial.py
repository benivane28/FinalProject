# Generated by Django 4.0.2 on 2022-02-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creadora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=2000)),
                ('foto', models.ImageField(upload_to='sobremi')),
            ],
            options={
                'verbose_name': 'creadora',
                'verbose_name_plural': 'creadoras',
            },
        ),
    ]
