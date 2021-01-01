# Generated by Django 3.1.4 on 2020-12-31 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=30)),
                ('Last_Name', models.CharField(max_length=30)),
                ('Age', models.CharField(max_length=30)),
                ('Nationality', models.CharField(max_length=30)),
                ('Freelance', models.CharField(default='Available', max_length=30)),
                ('Address', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=30)),
                ('Skype', models.CharField(max_length=30)),
                ('Langages', models.CharField(max_length=30)),
            ],
        ),
    ]
