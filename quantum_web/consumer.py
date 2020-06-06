# -*- coding: utf-8 -*-
import qboard

from channels.generic.websocket import WebsocketConsumer
from quantum_web.utils import solver, Q


class QuantConsumer(WebsocketConsumer):
    """Консьюмер вебсокетов."""

    def cb(self, dic):
        if dic["cb_type"] == qboard.constants.CB_TYPE_NEW_SOLUTION:
            self.send(str(dic['energy']))
        if dic["cb_type"] == qboard.constants.CB_TYPE_INTERRUPT_TIMEOUT:
            raise Exception("Solver interrupted by timeout")
        if dic["cb_type"] == qboard.constants.CB_TYPE_INTERRUPT_TARGET:
            raise Exception("Solver interrupted by target")

    def connect(self):
        self.accept()

    def receive(self, text_data=None, bytes_data=None):
        if text_data == 'start':
            solver.solve_qubo(Q, callback=self.cb, timeout=30, verbosity=0)
