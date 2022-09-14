from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProfileModelViewSet,UserModelViewSet

urlpatterns = [

]
router = DefaultRouter()
router.register(r'profile', ProfileModelViewSet)
router.register(r'user', UserModelViewSet)
urlpatterns += router.urls
