from django.urls import path
from .views import ReadingViews

urlpatterns = [
    path('', ReadingViews.as_view())
]