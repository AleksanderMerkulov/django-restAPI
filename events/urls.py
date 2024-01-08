from django.urls import path

from events.views import *

urlpatterns = [
    path('', EventsAPI.as_view()),
    path('<int:pk>/', EventDetailAPI.as_view())
]
