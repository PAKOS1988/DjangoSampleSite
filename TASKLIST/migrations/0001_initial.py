# Generated by Django 4.2.1 on 2023-05-04 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tasklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=150)),
                ('status', models.BooleanField(default=False)),
                ('datatime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
