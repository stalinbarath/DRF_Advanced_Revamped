from django.contrib import admin

# Register your models here.
from watchlist_app.models import Watchlist, Platform, Review

admin.site.register(Watchlist)
admin.site.register(Platform)
admin.site.register(Review)