from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Theme)
admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(Comment)