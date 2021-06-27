# Generated by Django 3.2.4 on 2021-06-27 16:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('book', models.TextField()),
                ('author', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
