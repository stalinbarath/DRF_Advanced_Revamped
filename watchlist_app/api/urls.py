from django.urls import path

from watchlist_app.api import views

urlpatterns = [
    path('list/', views.WatchlistCollection.as_view(), name = 'watchlist-list'),
    path('<int:pk>', views.WatchlistItem.as_view(), name = 'watchlist-detail'),
    path('platform/', views.StreamingPlatform.as_view(), name = 'platform-list'),
    path('platform/<int:pk>', views.PlatformItem.as_view(), name = 'platform-detail'),
    path('reviews/', views.ReviewList.as_view(), name = 'review-list'),
    path('reviews/<int:pk>', views.ReviewDetail.as_view(), name = 'review-detail'),
]
