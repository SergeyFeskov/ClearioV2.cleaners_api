# myapi/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('cleaners/', views.CleanersList.as_view()),
    path('cleaners/<int:pk>/', views.CleanerDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)