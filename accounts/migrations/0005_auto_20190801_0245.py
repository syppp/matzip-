# Generated by Django 2.2.1 on 2019-07-31 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190801_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputform',
            name='photo',
            field=models.ImageField(upload_to='board/'),
        ),
    ]