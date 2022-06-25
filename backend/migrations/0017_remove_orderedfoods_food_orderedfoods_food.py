# Generated by Django 4.0.1 on 2022-01-16 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0016_orderedfoods_address_orderedfoods_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedfoods',
            name='food',
        ),
        migrations.AddField(
            model_name='orderedfoods',
            name='food',
            field=models.ManyToManyField(blank=True, null=True, related_name='food', to='backend.Food'),
        ),
    ]
