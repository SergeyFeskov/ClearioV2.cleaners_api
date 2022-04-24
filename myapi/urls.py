# myapi/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CleanersInfoViewSet, ByOneCleanerViewSet

cleaners_list = CleanersInfoViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
cleaner_detail = CleanersInfoViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = DefaultRouter()
router.register(r'cleaners', CleanersInfoViewSet, basename="cleaners")
router.register(r'byone', ByOneCleanerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]