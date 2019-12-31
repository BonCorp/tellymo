from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tvshow import views


router = DefaultRouter()
router.register('tags', views.TagViewSet)

app_name = 'tvshow'

urlpatterns = [
    path('', include(router.urls))
]
