from django.http import request

from rest_framework import status, mixins, generics
from rest_framework.response import Response
from rest_framework.views import APIView

from watchlist_app.api import serializers
from watchlist_app.models import Watchlist, Platform, Review

class WatchlistCollection(APIView):

    def get(self, request):
        watchlist = Watchlist.objects.all()
        serializer = serializers.WatchlistSerializer(watchlist, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.WatchlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class WatchlistItem(APIView):

    def get(self, request, pk):
        watchlistitem = Watchlist.objects.get(pk=pk)
        serializer = serializers.WatchlistSerializer(watchlistitem)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            watchlistitem = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.WatchlistSerializer(watchlistitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk):
        try:
            watchlistitem = Watchlist.objects.get(pk=pk)
        except Watchlist.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_400_BAD_REQUEST)
        watchlistitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamingPlatform(APIView):

    def get(self, request):
        platform = Platform.objects.all()
        serializer = serializers.PlatformSerializer(platform, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.PlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

class PlatformItem(APIView):

    def get(self, request, pk):
        platformitem = Platform.objects.get(pk=pk)
        serializer = serializers.PlatformSerializer(platformitem, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            platformitem = Platform.objects.get(pk=pk)
        except Platform.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = serializers.PlatformSerializer(platformitem, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def delete(self, request, pk):
        try:
            platformitem = Platform.objects.get(pk=pk)
        except Platform.DoesNotExist:
            return Response({'error': 'Item not found'}, status=status.HTTP_400_BAD_REQUEST)
        platformitem.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer

class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = serializers.ReviewSerializer