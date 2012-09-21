# encoding: utf-8
# Copyright 2012 California Institute of Technology. ALL RIGHTS
# RESERVED. U.S. Government Sponsorship acknowledged.

from pkg_resources import resource_filename
from Products.CMFCore.interfaces import IFolderish
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.WorkflowCore import WorkflowException

def publish(item, wfTool=None):
    if wfTool is None:
        wfTool = getToolByName(item, 'portal_workflow')
    try:
        wfTool.doActionFor(item, action='publish')
        item.reindexObject()
    except WorkflowException:
        pass
    if IFolderish.providedBy(item):
        for itemID, subItem in item.contentItems():
            publish(subItem, wfTool)


def publishHomePage(portal):
    if 'front-page' not in portal.keys(): return
    publish(portal['front-page'])


def loadPhotographs(portal):
    if 'staff-photographs' in portal.keys(): return
    portal._importObjectFromFile(resource_filename(__name__, 'data/staff-photographs.zexp'))
    publish(portal['staff-photographs'])


def setupVarious(context):
    if context.readDataFile('edrndmcc.appserver.marker.txt') is None: return
    portal = context.getSite()
    publishHomePage(portal)
    loadPhotographs(portal)
