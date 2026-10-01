from django.urls import path, include
from rest_framework import routers

from .views import RollsViewSet


app_name = "api"

router = routers.DefaultRouter()

router.register(r'rolls', RollsViewSet)

urlpatterns = [
    path('', include(router.urls))
]