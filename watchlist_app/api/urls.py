from django.urls import path

from watchlist_app.api import views

urlpatterns = [
    path('list/', views.WatchlistCollection.as_view(), name = 'watchlistcollection'),
    path('<int:pk>', views.WatchlistItem.as_view(), name = 'watchlist-detail'),
    path('platform/', views.StreamingPlatform.as_view(), name = 'streamingplatform'),
    path('platform/<int:pk>', views.PlatformItem.as_view(), name = 'platform-detail'),
]
