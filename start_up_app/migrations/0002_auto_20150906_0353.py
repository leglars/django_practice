# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('start_up_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publisher',
            old_name='state_provinc',
            new_name='state_province',
        ),
    ]
