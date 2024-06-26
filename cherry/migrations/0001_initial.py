# Generated by Django 5.0.3 on 2024-04-08 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255, null=True)),
                ('password', models.CharField(default='1234', max_length=255)),
            ],
            options={
                'db_table': 'user_data-table',
            },
        ),
    ]
