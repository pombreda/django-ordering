'''
Created on Jun 3, 2011

@author: scheper
'''
from django.contrib.auth.models import User
from django.test import TestCase

from ordering.models import Selectable
from ordering.tests.models import TestProject, TestVendor


class ModelSmokeTests(TestCase):
    '''Very simple tests to ensure basic environment is working
    '''
    def test_environment(self):
        self.assert_(True)

class SelectableTests(TestCase):
    '''Some basic tests of Selectable model
    '''
    fixtures = [
        'src/ordering/tests/fixtures/users.yaml',
        'src/ordering/tests/fixtures/selectables.yaml',
    ]

    def test_unicode(self):
        '''Smoke test string representation of models'''
        self.assertEqual(u'<TestVendor: Foo Inc.>',
                repr(TestVendor.objects.get()))
        self.assertEqual(u'<TestProject: Project Bar>',
                repr(TestProject.objects.get()))

    def test_slug(self):
        '''Smoke test to check that a simple slug is correctly generated'''
        p = TestProject(text='Simple Project Foo',
                creator=User.objects.get(username='test_user'))
        self.assertEqual('', p.slug)    # unsaved model should have a slug of
                                        # empty string
        p.save()
        self.assertEqual(u'simple-project-foo', p.slug) # after saving, slug is
                                                        # populated

    def test_slug_uniqueness(self):
        '''Test that slugs are generated uniquely'''
        p = TestProject(text='Project Bar',
                creator=User.objects.get(username='test_user'))
        p.save()
        self.assertEqual(u'project-bar-2', p.slug)

        p = TestProject(text='Project Bar',
                creator=User.objects.get(username='test_user'))
        p.save()
        self.assertEqual(u'project-bar-3', p.slug)

    def test_manager(self):
        '''Smoke test SelectableManager is setup correctly'''
        self.assertEqual(2, Selectable.objects.count())
        self.assertEqual(1, TestProject.objects.count())
        self.assertEqual(1, TestVendor.objects.count())
