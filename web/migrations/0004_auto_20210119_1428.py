# Generated by Django 2.2 on 2021-01-19 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20210119_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loansdetails',
            name='fine',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='web.UserDetails')),
            ],
        ),
    ]
