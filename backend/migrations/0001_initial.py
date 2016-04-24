# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
# Generated by Django 1.9.1 on 2016-04-03 14:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('nick_name', models.CharField(default='', max_length=50)),
                ('location', models.CharField(default='', max_length=50)),
                ('visual_description', models.CharField(default='', max_length=200)),
                ('is_military', models.BooleanField(default=False)),
                ('duration_of_homelessness', models.IntegerField(default=0)),
                ('health_concerns', models.BooleanField(default=False)),
                ('dna_assistance', models.BooleanField(default=False)),
                ('has_doctor', models.BooleanField(default=False)),
                ('has_insurance', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(blank=True, default='', max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='', max_length=50)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.CharField(default='', max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interaction_client', to='backend.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Interaction_Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interaction_photos', to='backend.Interaction')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('amount', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('location', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asked_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('amount', models.IntegerField(default=0)),
                ('description', models.CharField(default='', max_length=200)),
                ('client_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='backend.Client')),
                ('comp_interaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_comp', to='backend.Interaction')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request', to='backend.Item')),
                ('src_interaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='request_src', to='backend.Interaction')),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(default='', max_length=50)),
                ('radius', models.IntegerField(default=1)),
                ('created_timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ManyToManyField(related_name='client_route', to='backend.Client')),
            ],
        ),
        migrations.CreateModel(
            name='Route_Item_Amounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('item', models.ManyToManyField(related_name='route_item', to='backend.Item')),
                ('route', models.ManyToManyField(related_name='route', to='backend.Route')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('tag_type', models.CharField(default='', max_length=50)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_tags', to='backend.Client')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('role', models.CharField(default='', max_length=50)),
                ('org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='backend.Organization')),
            ],
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse', to='backend.Organization')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_route', to='backend.User'),
        ),
        migrations.AddField(
            model_name='item',
            name='warehouse',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='warehouse_item', to='backend.Warehouse'),
        ),
        migrations.AddField(
            model_name='interaction',
            name='route',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interaction_route', to='backend.Route'),
        ),
        migrations.AddField(
            model_name='interaction',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interaction_user', to='backend.User'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='customuser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='client',
            name='case_manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_cm', to='backend.User'),
        ),
        migrations.AddField(
            model_name='client',
            name='followers',
            field=models.ManyToManyField(related_name='client_followers', to='backend.User'),
        ),
        migrations.AddField(
            model_name='client',
            name='org',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_org', to='backend.Organization'),
        ),
    ]
