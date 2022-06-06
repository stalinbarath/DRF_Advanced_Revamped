from rest_framework import serializers

from watchlist_app.models import Watchlist, Platform, Review

class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = "__all__"

class PlatformSerializer(serializers.HyperlinkedModelSerializer):
    # watchlist = WatchlistSerializer(many=True, read_only=True)
    watchlist = serializers.StringRelatedField(many=True, read_only=True)
    class Meta:
        model = Platform
        fields = "__all__"

class ReviewSerializer(serializers.ModelField):
    class Meta:
        model = Review
        fields = "__all__"