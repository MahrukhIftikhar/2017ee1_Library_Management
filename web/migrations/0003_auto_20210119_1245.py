# Generated by Django 2.2 on 2021-01-19 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20210118_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminDetails',
            fields=[
                ('login_id', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('SSN', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'administration',
            },
        ),
        migrations.AddField(
            model_name='staffdetails',
            name='password',
            field=models.CharField(default='NULL', max_length=255),
        ),
        migrations.AddField(
            model_name='staffsdetails',
            name='password',
            field=models.CharField(default='NULL', max_length=100),
        ),
        migrations.AlterField(
            model_name='loandetails',
            name='fine',
            field=models.IntegerField(),
        ),
    ]
