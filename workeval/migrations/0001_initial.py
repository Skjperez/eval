# Generated by Django 3.2.4 on 2021-06-28 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=50)),
                ('department', models.CharField(max_length=50)),
                ('reviewer_name', models.CharField(max_length=50)),
                ('questionarrie', models.CharField(max_length=200)),
            ],
        ),
    ]