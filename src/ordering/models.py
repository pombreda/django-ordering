'''
Created on Jun 3, 2011

@author: scheper
'''
from django.contrib.auth.models import User
from django.db import models
from ordering.utils import unique_slugify


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
