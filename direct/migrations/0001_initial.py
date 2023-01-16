# Generated by Django 4.1.5 on 2023-01-12 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialogue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='auth_user', to=settings.AUTH_USER_MODEL)),
                ('companion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companion', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Dialogue',
                'verbose_name_plural': 'Dialogues',
            },
        ),
        migrations.CreateModel(
            name='Massage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='massage', to=settings.AUTH_USER_MODEL)),
                ('dialogue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='massage', to='direct.dialogue')),
            ],
            options={
                'verbose_name': 'Massage',
                'verbose_name_plural': 'Massages',
                'ordering': ['-created_at'],
            },
        ),
    ]