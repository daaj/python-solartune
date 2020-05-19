from __future__ import absolute_import, unicode_literals

from django.db import models

from wagtail.wagtailcore.models import Page

# from wagtail.wagtailcore.fields import StreamField
# from wagtail.wagtailcore import blocks
# from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel
# from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailadmin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel


@register_snippet
class Technology(models.Model):
    url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)
    image = models.ForeignKey('wagtailimages.Image')
    panels = [
        FieldPanel('url'),
        FieldPanel('title'),
        ImageChooserPanel('image'),
    ]
    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('image'),
    ]

    def __str__(self):
        return self.title


class HomePage(Page):
    pass
