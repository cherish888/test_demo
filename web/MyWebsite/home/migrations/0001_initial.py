# Generated by Django 2.1.3 on 2018-12-20 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=10)),
                ('password', models.CharField(max_length=100)),
                ('name', models.TextField(default='')),
                ('user_email', models.CharField(max_length=100)),
                ('creat_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(default='')),
            ],
        ),
    ]
