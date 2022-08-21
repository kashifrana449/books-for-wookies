# Generated by Django 4.1 on 2022-08-21 09:43

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
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.CharField(blank=True, max_length=256, null=True)),
                ('price', models.IntegerField()),
                ('cover_image', models.CharField(blank=True, max_length=256, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', related_query_name='books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'books',
            },
        ),
    ]