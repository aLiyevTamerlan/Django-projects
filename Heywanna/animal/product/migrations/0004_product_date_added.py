# Generated by Django 3.2.7 on 2022-02-13 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_comment_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
