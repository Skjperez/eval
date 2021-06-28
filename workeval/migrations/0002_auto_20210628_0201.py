# Generated by Django 3.2.4 on 2021-06-28 02:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workeval', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='EvaluationTemplateQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
                ('evaluation_template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workeval.evaluationtemplate')),
            ],
        ),
        migrations.DeleteModel(
            name='Evaluation',
        ),
    ]