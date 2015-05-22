# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import modelcluster.fields
import wagtail.wagtailcore.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0010_change_page_owner_to_null_on_delete'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicBlock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.SlugField(unique=True, max_length=255, blank=True)),
                ('heading', models.CharField(max_length=255, null=True, blank=True)),
                ('name', models.CharField(max_length=255)),
                ('text', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
                'verbose_name': 'Block',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BasicBlockPlacement',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.IntegerField(null=True, editable=False, blank=True)),
                ('block', models.ForeignKey(related_name='+', to='basic_site.BasicBlock')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BasicPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='BasicPageListing',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='basicblockplacement',
            name='page',
            field=modelcluster.fields.ParentalKey(related_name='blocks', to='wagtailcore.Page'),
            preserve_default=True,
        ),
    ]
