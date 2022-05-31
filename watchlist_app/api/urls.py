from django.urls import path

from watchlist_app.api import views

urlpatterns = [
    path('list/', views.WatchlistCollection.as_view(), name = 'watchlistcollection'),
    path('<int:pk>', views.WatchlistItem.as_view(), name = 'watchlistitem')
]
