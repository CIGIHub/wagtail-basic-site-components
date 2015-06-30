# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks
import wagtail.wagtailimages.blocks
from django.db import migrations, models

import basic_site.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0001_squashed_0016_change_page_url_path_to_text_field'),
        ('basic_site', '0004_basicblock_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='BasicStreamPage',
            fields=[
                ('page_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', basic_site.fields.BodyField([('Heading', wagtail.wagtailcore.blocks.CharBlock(classname='heading', icon='title')), ('Paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='doc-full')), ('Image', wagtail.wagtailimages.blocks.ImageChooserBlock(icon='image')), ('Embed', wagtail.wagtailembeds.blocks.EmbedBlock(icon='site')), ('List', wagtail.wagtailcore.blocks.ListBlock(wagtail.wagtailcore.blocks.RichTextBlock(label='item'), icon='list-ul'))])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
