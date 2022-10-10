# Generated by Django 4.1.1 on 2022-09-30 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('voters', '0001_initial'),
        ('polls', '0001_initial'),
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.poll')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voters.voter')),
            ],
            options={
                'db_table': 'Votes Table',
                'ordering': ['-created_date'],
            },
        ),
    ]
