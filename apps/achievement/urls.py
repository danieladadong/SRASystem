from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

urlpatterns = [
    path('stat/',AchievementStatistics.as_view()),
    path('ptat/',PatentStatistics.as_view()),
    path('papertat/',PaperStatistics.as_view()),
    path('ajtat/',AjStatistics.as_view())
]
router = DefaultRouter()
router.register(r'acmonograph', AcmonographModelViewSet)
router.register(r'acjournals', AcjournalsModelViewSet)
router.register(r'paper', PaperModelViewSet)
router.register(r'patent', PatentModelViewSet)
router.register(r'achievement', AchievementModelViewSet)
urlpatterns += router.urls
