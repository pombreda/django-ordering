'''
Created on Jun 3, 2011

@author: scheper
'''
from django.db import models

from ordering.models import BaseItem, BaseOrder, Selectable, SelectableManager


class TestItem(BaseItem):
    vendor = models.ForeignKey('TestVendor')

class TestOrder(BaseOrder):
    item = models.ForeignKey('TestItem', related_name='orders',
                             help_text='Item being ordered')

    def __unicode__(self):
        return u'%s (%s)' % (self.creator, self.item.description)

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
