from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FundModelViewSet, ProjectModelViewSet, DynamicModelViewSet

urlpatterns = [

]
router = DefaultRouter()
router.register(r'fund', FundModelViewSet)
router.register(r'project', ProjectModelViewSet)
router.register(r'dynamic', DynamicModelViewSet)
urlpatterns += router.urls
