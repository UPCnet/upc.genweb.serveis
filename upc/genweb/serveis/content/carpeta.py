"""Definition of the SERVEI3.0 content type.
"""
__author__ = """José Luis Vivanco C <jose.luis.vivanco@upcnet.es>"""
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.component import adapts

from Products.CMFCore.utils import getToolByName, _checkPermission
from Products.Archetypes.interfaces import IObjectPostValidation

from Products.Archetypes.atapi import *
from AccessControl import ClassSecurityInfo

from Products.Archetypes.public import DisplayList
from Products.Archetypes.public import *

from Products.ATContentTypes.content.document import ATDocument
from Products.ATContentTypes.content.folder import ATFolder

from upc.genweb.serveis.interfaces import ICarpeta
from upc.genweb.serveis.config import PROJECTNAME

Carpetasch = getattr(ATFolder, 'schema', Schema(())).copy() + \
    getattr(ATDocument, 'schema', Schema(())).copy()

Carpetasch['description'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
Carpetasch['relatedItems'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}


class Carpeta(OrderedBaseFolder, ATFolder, ATDocument):
    """
    Documento para describir un servicio
    """

    security = ClassSecurityInfo()
    implements(ICarpeta)

    meta_type = 'Carpeta'
    _at_rename_after_creation = True

    schema = Carpetasch

    def muestranotif(self):
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Notificacions',sort_order='reverse',sort_on='getFechaincidencia',review_state='published')
        return mt
        
registerType(Carpeta, PROJECTNAME)
