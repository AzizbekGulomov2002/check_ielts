from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter


from .views import PupilViewset


router = DefaultRouter()
router.register('pupils',PupilViewset)

urlpatterns = [
    path('', include(router.urls))
]
