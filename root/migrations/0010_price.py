# Generated by Django 4.2 on 2024-08-07 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0009_rename_statusf_vijegi_text_remove_vijegi_statust_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descrip', models.TextField(default='No descriptions.')),
                ('price', models.IntegerField()),
                ('time', models.CharField(max_length=100)),
            ],
        ),
    ]
