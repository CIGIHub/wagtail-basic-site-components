# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_site', '0002_auto_20150513_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basicblockplacement',
            old_name='blocks',
            new_name='block',
        ),
    ]
