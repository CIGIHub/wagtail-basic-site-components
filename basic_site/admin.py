from django.contrib import admin

from . import models

admin.site.register(models.BasicPage)
admin.site.register(models.BasicPageListing)
admin.site.register(models.BasicBlock)
admin.site.register(models.BasicBlockPlacement)
