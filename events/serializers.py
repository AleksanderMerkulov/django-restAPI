from rest_framework import serializers

from events.models import Events


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ('title', 'desc', 'category')
