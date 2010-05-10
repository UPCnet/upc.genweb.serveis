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

    def serveis_ordenats(self):
        #import time
        #aux = time.time()
        portal_catalog = getToolByName(self, 'portal_catalog')
        lista_faqs = portal_catalog.searchResults(portal_type = 'ServeiFaq',sort_order = 'sortable_title',review_state='published')
        dic_faqs = {}
        for faq in lista_faqs:
          serveis_faq = faq.getListaservei2
          for servei in serveis_faq:
            if dic_faqs.has_key(servei):
              dic_faqs[servei].append(faq)
            else:
              dic_faqs[servei] = [faq]
        #return time.time() - aux #0.00395894050598 s

        claus = sorted(dic_faqs, key=str.lower)
        resultat = []
        for c in claus:
            entrada = [c, dic_faqs[c]]
            resultat.append(entrada)
        #return time.time() - aux #0.00398802757263 s
        return resultat


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
