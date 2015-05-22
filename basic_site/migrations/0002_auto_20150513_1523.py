# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_site', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basicblockplacement',
            old_name='block',
            new_name='blocks',
        ),
    ]
