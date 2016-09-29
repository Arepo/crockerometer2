from __future__ import absolute_import
from django.contrib import admin
from .models import Metric, Vote, Woojit

# Register your models here.
admin.site.register(Metric)
admin.site.register(Vote)
admin.site.register(Woojit)
