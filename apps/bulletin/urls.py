from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AnnouncementModelViewSet,AcademicexchangeModelViewSet
urlpatterns=[

]
router = DefaultRouter()
router.register(r'announcement',AnnouncementModelViewSet)
router.register(r'acexchange',AcademicexchangeModelViewSet)
urlpatterns += router.urls