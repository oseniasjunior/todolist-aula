from django.urls import path
from core import consumers

urlrouter = [
    path('ws/test/', consumers.Consumer.as_asgi())
]