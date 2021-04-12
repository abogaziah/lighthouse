from django.urls import path

from .views import MissingPersonViewSet

urlpatterns = [
    path('missing', MissingPersonViewSet.as_view({
        'get': 'view',
        'post': 'create'
    })),
    path('missing/<str:pk>', MissingPersonViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    })),
]