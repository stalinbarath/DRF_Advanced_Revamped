from django.contrib import admin

# Register your models here.
from watchlist_app.models import Watchlist, Platform

admin.site.register(Watchlist)
admin.site.register(Platform)