# Generated by Django 3.2.7 on 2022-03-26 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0011_rename_message_notice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Own',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('mehsul_sahibi', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('sahiblenen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sahiblenen', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]