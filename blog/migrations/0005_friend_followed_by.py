# Generated by Django 3.2.16 on 2023-01-09 03:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_auto_20230109_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='followed_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='followed_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
