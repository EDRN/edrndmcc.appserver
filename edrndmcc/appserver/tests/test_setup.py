# encoding: utf-8
# Copyright 2008 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

'''Tests for the setup of the site policy.
'''

import unittest2 as unittest
from Products.CMFCore.utils import getToolByName
from edrndmcc.appserver.testing import EDRN_DMCC_APP_SERVER_FUNCTIONAL_TESTING

class SetupTest(unittest.TestCase):
    '''Unit tests the setup of the site policy.'''
    layer = EDRN_DMCC_APP_SERVER_FUNCTIONAL_TESTING
    def setUp(self):
        super(SetupTest, self).setUp()
        self.portal = self.layer['portal']
    def testPortalTitle(self):
        '''Test if the site's title is set correctly.'''
        self.assertEquals('EDRN DMCC Application Server', self.portal.getProperty('title'))
    def testPortalDescription(self):
        '''Test if the site's description is set correctly.'''
        self.assertEquals('Application server for the Data Management and Coordinating Center (DMCC) of the Early Detection Research Network (EDRN).', self.portal.getProperty('description'))
    def testNASAResponsibleParties(self):
        '''Test if the NASA-mandated responsible party names are set correctly.'''
        self.assertEquals('Sean Kelly', self.portal.getProperty('executive_editor'))
        self.assertEquals('Dan Crichton', self.portal.getProperty('nasa_official'))
    def testIfEDRNRDFServiceAvailable(self):
        types = getToolByName(self.portal, 'portal_types')
        self.failUnless('Body System' in types.objectIds(), 'EDRN RDF Service not installed')
    def testIfThemeInstalled(self):
      skins = getToolByName(self.portal, 'portal_skins')
      layer = skins.getSkinPath('EDRN Theme')
      self.failUnless(layer, 'Theme layer missing from skins tool')
      self.assertEquals('EDRN Theme', skins.getDefaultSkin(), 'EDRN theme not default skin')
    
def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
