# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-10 06:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='ContactData',
        ),
    ]
