# Generated by Django 3.0.2 on 2020-01-02 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=6)),
                ('redirect_location', models.CharField(max_length=256)),
                ('expiration_date', models.DateTimeField()),
                ('author_ip', models.GenericIPAddressField()),
                ('is_active', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='LinkOpening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opener_ip_address', models.GenericIPAddressField()),
                ('open_datetime', models.DateTimeField()),
                ('link_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Link')),
            ],
        ),
    ]
