from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EntryAwardsModelViewSet, AchievementAwardModelViewSet

urlpatterns = [

]
router = DefaultRouter()
router.register(r'entryawards', EntryAwardsModelViewSet)
router.register(r'achievementaward', AchievementAwardModelViewSet)
urlpatterns += router.urls
