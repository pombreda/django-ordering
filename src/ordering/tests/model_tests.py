'''
Created on Jun 3, 2011

@author: scheper
'''
from django.test import TestCase


class ModelSmokeTests(TestCase):
    '''Very simple tests to ensure basic environment is working
    '''

    def test_environment(self):
        self.assert_(True)
