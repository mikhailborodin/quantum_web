# -*- coding: utf-8 -*-

import qboard
import numpy as np

Q = np.random.rand(30, 30) - 0.5

solver = qboard.solver(mode="bf")
