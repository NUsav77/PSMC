# Generated by Django 3.2 on 2021-04-20 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SavBlock', '0004_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
