# -*- coding: utf-8 -*-
from neuron import Neuron
and2neuron = Neuron(2)

# b=w0=-1.5 = смещение, w1=1.0, w2=1.0

weights = [0.5, -1.0]
and2neuron.set_weights(weights)

# тестирование
test_vector = [0.0]
and2neuron.cal_y(test_vector)
print(and2neuron.get_y())

test_vector = [1.0]
and2neuron.cal_y(test_vector)
print(and2neuron.get_y())