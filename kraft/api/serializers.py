from rest_framework import serializers

from production.models import Roll


class RollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roll
        fields = ('number', 'weight')