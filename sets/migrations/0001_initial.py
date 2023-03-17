# Generated by Django 4.1.7 on 2023-03-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='card_set',
            fields=[
                ('id', models.CharField(max_length=512, primary_key=True, serialize=False)),
                ('images', models.JSONField(default=None, null=True)),
                ('legalities', models.JSONField(default=None, null=True)),
                ('name', models.CharField(max_length=512)),
                ('printedTotal', models.SmallIntegerField(default=None, null=True)),
                ('ptcgoCode', models.CharField(default=None, max_length=512, null=True)),
                ('releaseDate', models.DateField(default=None, null=True)),
                ('series', models.CharField(default=None, max_length=512, null=True)),
                ('total', models.SmallIntegerField(default=None, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]