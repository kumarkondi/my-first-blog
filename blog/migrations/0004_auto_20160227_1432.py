# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 09:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='author',
            new_name='name',
        ),
    ]