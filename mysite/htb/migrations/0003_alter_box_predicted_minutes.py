# Generated by Django 3.2.20 on 2023-12-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htb', '0002_box_authuserinrootowns'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='predicted_minutes',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
