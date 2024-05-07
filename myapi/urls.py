from django.urls import include, path
from .views import TownListView , ShortestPathVisualization
from rest_framework import routers
router = routers.DefaultRouter()




urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Assuming you have the admin URLs included
    path('town/', TownListView.as_view(), name='town-list'),
    path('shortest-path/<str:source_town>/<str:target_town>/', ShortestPathVisualization.as_view(), name='shortest-path'),
]
