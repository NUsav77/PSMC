# Generated by Django 3.2 on 2021-04-20 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SavBlock', '0003_auto_20210419_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
