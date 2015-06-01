from __future__ import absolute_import
from __future__ import unicode_literals

import re

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.html import strip_tags
from django.utils.text import slugify
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import FieldPanel, InlinePanel
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtailsearch import index
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailsnippets.models import register_snippet


class UniquelySlugable(models.Model):
    slug = models.SlugField(max_length=255, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:255]

            while type(self).objects.filter(slug=self.slug).exists():
                match_obj = re.match(r'^(.*)-(\d+)$', self.slug)
                if match_obj:
                    next_int = int(match_obj.group(2)) + 1
                    self.slug = match_obj.group(1) + "-" + str(next_int)
                else:
                    self.slug += '-2'

        super(UniquelySlugable, self).save(*args, **kwargs)


# create a base snippet with basic fields
class BaseBlock(UniquelySlugable):
    heading = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255)
    text = RichTextField()

    class Meta:
        abstract = True


# create a snippet for placement in sidebars
@register_snippet
@python_2_unicode_compatible
class BasicBlock(BaseBlock):

    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('heading'),
        FieldPanel('text'),
        ImageChooserPanel('image'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Block'


class BasicBlockPlacement(Orderable, models.Model):
    page = ParentalKey('wagtailcore.Page', related_name='blocks')
    block = models.ForeignKey('basic_site.BasicBlock', related_name='+')

    panels = [
        SnippetChooserPanel('block', BasicBlock),
    ]


# create a base page that adds a body field
@python_2_unicode_compatible
class BasePage(models.Model):
    body = RichTextField()

    search_fields = Page.search_fields + (
        index.SearchField('body'),
    )

    def __str__(self):
        return "{} - {}".format(self.title, self.url)

    class Meta:
        abstract = True


# create a basic page type
class BasicPage(Page, BasePage):
    pass

BasicPage.content_panels = [
    FieldPanel('title', classname="title"),
    FieldPanel('body', classname="full"),
    InlinePanel(BasicPage, 'blocks', label='Blocks'),
]


# create a listing for basic pages
@python_2_unicode_compatible
class BasicPageListing(Page):
    subpage_types = ['BasicPage']

    @property
    def subpages(self):
        # Get list of live signage pages that are descendants of this page
        subpages = BasicPage.objects.live().descendant_of(self)

        return subpages

    def __str__(self):
        return "{} - {}".format(self.title, self.url)  # create a snippet that is embedded directly into a template

    def embedded_content_for_search(self):
        contents = strip_tags('/n'.join(
            ['/n'.join(value)
             for value in self.subpages.all().values_list(
                'title', 'body')]))
        return contents

    search_fields = Page.search_fields + (
        index.SearchField('embedded_content_for_search'),
    )

    def search_result_text(self):
        return "TODO: Basic Page Listing description"


BasicPageListing.content_panels = [
    FieldPanel('title', classname="title"),
    InlinePanel(BasicPageListing, 'blocks', label='Blocks'),
]
