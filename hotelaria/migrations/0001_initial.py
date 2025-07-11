# Generated by Django 5.2.4 on 2025-07-03 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospede',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CPF', models.IntegerField(unique=True)),
                ('data_nascimento_hospede', models.DateField()),
                ('login_hospede', models.CharField(max_length=50, unique=True)),
                ('senha_hospede', models.CharField(max_length=50)),
                ('email_hospede', models.EmailField(max_length=254, unique=True)),
                ('nome_hospede', models.CharField(max_length=100)),
            ],
        ),
    ]
