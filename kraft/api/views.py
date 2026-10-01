from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import RollSerializer
from .pagination import KraftPagination
from production.models import Roll


class RollsViewSet(ReadOnlyModelViewSet):
    """Отображение рола"""
    queryset = Roll.objects.all()
    serializer_class = RollSerializer
    pagination_class = KraftPagination
