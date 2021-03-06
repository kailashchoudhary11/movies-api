# Generated by Django 3.2.13 on 2022-06-29 13:19

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=500)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=4)),
                ('released_year', models.IntegerField()),
                ('genres', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
    ]
