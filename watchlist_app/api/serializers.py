from rest_framework import serializers

from watchlist_app.models import Watchlist, Platform

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = "__all__"

class PlatformSerializer(serializers.ModelSerializer):
    watchlist = WatchlistSerializer(many=True, read_only=True)
    class Meta:
        model = Platform
        fields = "__all__"