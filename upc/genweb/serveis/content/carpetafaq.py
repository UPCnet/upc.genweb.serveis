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

from upc.genweb.serveis.interfaces import ICarpetafaq
from upc.genweb.serveis.config import PROJECTNAME


Carpetaschf = getattr(ATFolder, 'schema', Schema(())).copy() + \
    getattr(ATDocument, 'schema', Schema(())).copy()

Carpetaschf['description'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
Carpetaschf['relatedItems'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
   
class Carpetafaq(OrderedBaseFolder, ATFolder, ATDocument):
    """
    Documento para describir un servicio
    """

    implements(ICarpetafaq)

    meta_type = 'Carpetafaq'
    _at_rename_after_creation = True

    schema = Carpetaschf

    def muestra_serv(self):
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Servei',sort_on='sortable_title',review_state='published')
        return mt
           
    def arregloobj(self,lista):
        tmp=lista
        new_list=[]
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Servei')       
        for i in tmp:
            for j in mt:
                if i==j.Title:
                    new_list.append(j)
        return new_list
    ### VERSION FINAL
    def enlacefaqv1(self,var):
        lista=[]
        obj=[] 
        portal_catalog = getToolByName(self, 'portal_catalog')          
        lista_faqs = portal_catalog.searchResults(portal_type = 'ServeiFaq',sort_order = 'sortable_title',review_state='published')              
        for i in lista_faqs:
            lista = i.getListaservei2
            lista1 = self.arregloobj(lista)                     
            for ii in lista1:
                if ii.getId==var:
                    obj.append(i)
        return obj
    
registerType(Carpetafaq, PROJECTNAME)
