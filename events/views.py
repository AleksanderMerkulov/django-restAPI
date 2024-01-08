from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response

from events.models import Events
from events.serializers import EventSerializer


# Create your views here.
class EventsAPI(generics.ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer

    # перегрузка функции post
    # сделал так, чтобы если пользователь не авторизован, то нельзя добавить новые поля
    def post(self, request, *args, **kwargs):
        print(request.user.is_authenticated)
        if request.user.is_authenticated:
            return self.create(request, *args, **kwargs)
        else:
            return Response({"error": "not allowed"})


class EventDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
