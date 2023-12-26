# Generated by Django 3.2.20 on 2023-12-26 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htb', '0003_alter_box_predicted_minutes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('boxes', models.ManyToManyField(to='htb.Box')),
            ],
        ),
    ]
