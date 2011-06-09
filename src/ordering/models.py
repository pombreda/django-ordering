'''
Created on Jun 3, 2011

@author: scheper
'''
from django.contrib.auth.models import User
from django.db import models
from ordering.utils import unique_slugify


class BaseItem(models.Model):
    '''Items that are ordered
    '''
    cost = models.DecimalField(max_digits=12, decimal_places=2,
            help_text='Cost of item')
    description = models.TextField(help_text='Description of item')
    slug = models.SlugField(blank=True, unique=True)
    creator = models.ForeignKey(User, help_text='User who created the model')
    created = models.DateTimeField(auto_now_add=True,
            help_text='When model was created')
    updated = models.DateTimeField(auto_now=True,
            help_text='When model was last updated')

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        '''Set slug field if it is None
        '''
        if not self.slug:
            unique_slugify(self, self.description)
        super(BaseItem, self).save(*args, **kwargs)

class BaseOrder(models.Model):
    '''Tracks data about individual orders
    '''
    creator = models.ForeignKey(User, related_name='orders_created',
            help_text='User who created this order request')
    ordered_by = models.ForeignKey(User, related_name='orders_placed',
            help_text='User who placed the order')
    quantity = models.PositiveIntegerField(help_text='Quantity of items to '
            'order')
    notes = models.TextField(help_text='Additional notes about order')
    created = models.DateTimeField(auto_now_add=True,
            help_text='Date order was created')
    updated = models.DateTimeField(auto_now=True,
            help_text='Date order was last updated')
    ordered = models.DateField(blank=True, null=True,
            help_text='Date order was placed')
    received = models.DateField(blank=True, null=True,
            help_text='Date order was received')

    class Meta:
        abstract = True

    def _calculate_cost(self):
        return self.item.cost * self.quantity

    cost = property(_calculate_cost)

class SelectableManager(models.Manager):
    '''Custom Manager for Selectable objects.
    '''
    def __init__(self, type=None):
        super(SelectableManager, self).__init__()
        self.type = type

    def get_query_set(self):
        query_set = super(SelectableManager, self).get_query_set()
        if self.type:
            query_set = query_set.filter(type=self.type)
        return query_set

class Selectable(models.Model):
    '''Selectable items that can be added to Items or Orders
    '''
    _TYPE = None

    text = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    slug = models.SlugField(blank=True, unique=True)
    creator = models.ForeignKey(User, help_text='User who created the model')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.text

    def save(self, *args, **kwargs):
        # Set _TYPE
        if self._TYPE is not None:
            self.type = self._TYPE
        # Set slug
        if not self.slug:
            unique_slugify(self, self.text)
        super(Selectable, self).save(*args, **kwargs)
