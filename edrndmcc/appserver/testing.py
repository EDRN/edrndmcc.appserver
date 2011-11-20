# encoding: utf-8
# Copyright 2011 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from edrn.rdf.testing import EDRN_RDF
from plone.app.testing import PloneSandboxLayer, IntegrationTesting, FunctionalTesting, PLONE_FIXTURE
from plone.testing import z2

class EDRN_DMCC_AppServerLayer(PloneSandboxLayer):
    defaultBases = (EDRN_RDF, PLONE_FIXTURE,)
    def setUpZope(self, app, configurationContext):
        import edrndmcc.appserver
        self.loadZCML(package=edrndmcc.appserver)
        z2.installProduct(app, 'edrndmcc.appserver')
    def setUpPloneSite(self, portal):
        self.applyProfile(portal, 'edrndmcc.appserver:default')
    def tearDownZope(self, app):
        z2.uninstallProduct(app, 'edrndmcc.appserver')

    
EDRN_DMCC_APP_SERVER = EDRN_DMCC_AppServerLayer()
EDRN_DMCC_APP_SERVER_INTEGRATION_TESTING = IntegrationTesting(
    bases=(EDRN_DMCC_APP_SERVER,),
    name='EDRN_DMCC_APP_SERVER:Integration'
)
EDRN_DMCC_APP_SERVER_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(EDRN_DMCC_APP_SERVER,),
    name='EDRN_DMCC_APP_SERVER:Functional'
)
