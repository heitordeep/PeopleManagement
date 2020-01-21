# Generated by Django 3.0.2 on 2020-01-20 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('descripion', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('salary', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Salary')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='people_management.Company')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
                ('email', models.EmailField(max_length=70, verbose_name='Email')),
                ('phone', models.CharField(max_length=15, verbose_name='Telephone')),
                ('status', models.BooleanField(default=True, verbose_name='Status')),
                ('bio', models.TextField(max_length=500, verbose_name='Bio')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('jobs', models.ManyToManyField(to='people_management.Jobs')),
            ],
        ),
    ]
