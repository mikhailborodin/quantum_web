# -*- coding: utf-8 -*-

from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

from quantum_web.consumer import QuantConsumer

websockets = URLRouter([
    path('ws/', QuantConsumer, name='ws_quants'),
])


application = ProtocolTypeRouter({
    'websocket': websockets,
})
