# -*- coding: utf-8 -*-

# Copyright 2018 IBM.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =============================================================================

import unittest

from parameterized import parameterized
from qiskit import QuantumRegister
from test.common import QiskitAquaTestCase
from qiskit_aqua.components.reciprocals.lookup_rotation import LookupRotation


class TestLookupRotation(QiskitAquaTestCase):
    """Lookup Rotation tests."""

    #def setUp(self):

    @parameterized.expand([[3, 344], [5, 1540], [7, 5678],
                           [9, 9728], [11, 14428]])
    def test_lookup_rotation(self, reg_size, gate_cnt):
        self.log.debug('Testing Lookup Rotation with positive eigenvalues')

        a = QuantumRegister(reg_size, name='a')
        lrot = LookupRotation(negative_evals=False)
        lrot_circuit = lrot.construct_circuit('', a)
        circuit_cnt = lrot_circuit.data.__len__()
        assert(circuit_cnt == gate_cnt)

        self.log.debug('Lookup rotation register size: {}'.format(reg_size))
        self.log.debug('Lookup rotation gate count:    {}'.format(circuit_cnt))

    @parameterized.expand([[3, 193], [5, 793], [7, 3817],
                           [9, 7725], [11, 11985]])
    def test_lookup_rotation_neg(self, reg_size, gate_cnt):
        self.log.debug('Testing Lookup Rotation with support for negative '
                       'eigenvalues')

        a = QuantumRegister(reg_size, name='a')
        lrot = LookupRotation(negative_evals=True)
        lrot_circuit = lrot.construct_circuit('', a)
        circuit_cnt = lrot_circuit.data.__len__()
        assert(circuit_cnt == gate_cnt)

        self.log.debug('Lookup rotation register size: {}'.format(reg_size))
        self.log.debug('Lookup rotation gate count:    {}'.format(circuit_cnt))


if __name__ == '__main__':
    unittest.main()