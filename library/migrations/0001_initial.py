# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=70)),
                ('author', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('keywords', models.TextField()),
                ('isbn', models.CharField(max_length=13)),
                ('ddn', models.CharField(max_length=10)),
                ('lcn', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('checkout_date', models.DateTimeField(verbose_name=b'Checkout Date')),
                ('due_date', models.DateTimeField(verbose_name=b'Due Date')),
                ('refreshes_remaining', models.IntegerField(default=0)),
                ('fees_assessed', models.DecimalField(max_digits=5, decimal_places=2)),
                ('fees_charged', models.DecimalField(max_digits=5, decimal_places=2)),
                ('book', models.ForeignKey(to='library.Book')),
                ('patron', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
