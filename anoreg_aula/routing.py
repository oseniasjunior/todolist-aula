from django.urls import path
from core import consumers

urlrouter = [
    path('ws/', consumers.Consume.as_asgi())
]