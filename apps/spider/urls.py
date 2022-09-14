from rest_framework.routers import DefaultRouter
from .views import JournalsView
from django.urls import path
urlpatterns = [
    path('journals/',JournalsView.as_view()),
]
router = DefaultRouter()
urlpatterns += router.urls