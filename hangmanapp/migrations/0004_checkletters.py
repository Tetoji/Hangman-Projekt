# Generated by Django 4.0.5 on 2022-09-05 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hangmanapp', '0003_aktivword'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckLetters',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkedLetters', models.CharField(max_length=500)),
            ],
        ),
    ]
