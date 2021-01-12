# Generated by Django 3.1.4 on 2021-01-12 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageSize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('length', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Shipping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=14)),
                ('email', models.EmailField(max_length=254)),
                ('street_address', models.CharField(max_length=30)),
                ('village', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
                ('location', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='packages.shippinglocation')),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[(1, 'Envelope'), (2, 'Parcel'), (3, 'Soft'), (4, 'Freezed')], default='1', max_length=1)),
                ('status', models.CharField(choices=[(1, 'WITH SUPLIER'), (2, 'AT GREEN MILE HUB'), (3, 'REBUNDLING'), (4, 'ON FLEET'), (5, 'DELIVERED')], default='1', max_length=1)),
                ('size', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='packages.packagesize')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='users.supplier')),
                ('to', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='packages.shipping')),
            ],
        ),
    ]
