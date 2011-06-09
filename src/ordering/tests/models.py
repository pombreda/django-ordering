'''
Created on Jun 3, 2011

@author: scheper
'''
from django.db import models

from ordering.models import BaseItem, Selectable, SelectableManager


class TestItem(BaseItem):
    vendor = models.ForeignKey('TestVendor')

class TestVendor(Selectable):
    _TYPE = u'TEST_VENDOR'
    objects = SelectableManager(type=_TYPE)

    class Meta:
        proxy = True

class TestProject(Selectable):
    _TYPE = u'TEST_PROJECT'
    objects = SelectableManager(type=_TYPE)

    class Meta:
        proxy = True
