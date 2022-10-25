# Generated by Django 4.0.3 on 2022-10-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name',models.CharField(max_length=25,db_index=True,default='any_name')),
                ('decs',models.CharField(max_length=50,db_index=True,default='description')),
                ('price',models.FloatField(db_index=True)),
                ('image',models.ImageField(upload_to='image')),

            ],
        ),
    ]