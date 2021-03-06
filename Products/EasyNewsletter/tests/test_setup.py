# -*- coding: utf-8 -*-
from Products.EasyNewsletter.testing import EASYNEWSLETTER_INTEGRATION_TESTING
from plone.app.testing import TEST_USER_ID
from plone.app.testing import setRoles
import unittest2 as unittest


class EasyNewsletterSetupTests(unittest.TestCase):

    layer = EASYNEWSLETTER_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.portal.invokeFactory('Folder', 'test-folder')
        self.folder = self.portal['test-folder']

        self.properties = self.portal.portal_properties

    def test_newsletter_factory(self):
        self.folder.invokeFactory("EasyNewsletter", "newsletter")
        self.assertEqual(
            'EasyNewsletter', self.folder.newsletter.portal_type)

    def test_catalog(self):
        indexes = self.portal.portal_catalog.indexes()
        self.assertEqual('email' in indexes, True)
        self.assertEqual('fullname' in indexes, True)
        self.assertEqual('organization' in indexes, True)

    def test_newsletter_subtypes_in_meta_types_not_to_list(self):
        # Hide newsletter subtypes from navigation
        self.assertTrue(
            self.properties.navtree_properties.hasProperty(
                'metaTypesNotToList'))
        metaTypesNotToList = \
            self.properties.navtree_properties.metaTypesNotToList
        self.assertTrue(
            'ENLIssue' in metaTypesNotToList)
        self.assertTrue(
            'ENLSubscriber' in metaTypesNotToList)
        self.assertTrue(
            'ENLTemplate' in metaTypesNotToList)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
