# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False, help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(max_length=20, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')], unique=True)),
                ('email', models.EmailField(verbose_name='email address', max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, null=True, max_length=30)),
                ('last_name', models.CharField(blank=True, null=True, max_length=50)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(verbose_name='groups', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
