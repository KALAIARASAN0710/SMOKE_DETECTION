from django.contrib import admin

# Register your models here.
from .models import WebsiteLink,SmokeDetection

admin.site.register(WebsiteLink)

admin.site.register(SmokeDetection)