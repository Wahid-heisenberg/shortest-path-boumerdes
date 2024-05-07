from django.urls import include, path
from .views import TownListView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # Assuming you have the admin URLs included
    path('town/', TownListView.as_view(), name='town-list'),
    # Add a default path to handle requests to the root URL
    path('', TownListView.as_view(), name='home'),  # Adjust this to match your requirements
]
