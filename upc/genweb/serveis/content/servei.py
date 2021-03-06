# -*- coding: utf-8 -*-
"""Definition of the SERVEI3.0 content type.
"""
__author__ = """Jose Luis Vivanco C <jose.luis.vivanco@upcnet.es>"""
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

from upc.genweb.serveis.interfaces import IServei
from upc.genweb.serveis.config import PROJECTNAME

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin
from Products.DataGridField import DataGridField, DataGridWidget
from Products.DataGridField.Column import Column
from Products.DataGridField.SelectColumn import SelectColumn


schema = Schema((

        DataGridField(
            name='availableAreas',
            widget=DataGridWidget(
                label="Enlaces",
                description="Enter the title for the link.",
                column_names=('Title', 'Url',),
                i18n_domain='Servei',
            ),
            required=True,
            columns=('title', 'url',)
        ),  
   
         LinesField('listaservei1',
                    required=False,
                    vocabulary='listaServiciosfinal',
                    enforceVocabulary=True,
                    widget=InAndOutWidget(
                            label="Lista de Servicios",
                            label_msgid="label_custom_view_fields",
                            description="Select which fields to display when "
                            "'Display as Table' is checked.",
                            description_msgid="help_custom_view_fields",),
         ),
         
         BooleanField(
                      name='contratomarco',
                      default=False,
                      widget=BooleanWidget(
                               label="Contracte Marc",
                               description="Sel·lecciona un servei relacionat amb el Contracte Marc",
                               label_msgid='Servei_Contrato_Marco',
                               description_msgid='Servei_Contrato_Marco',
                               i18n_domain='Servei',)
    ),
    
),
)


ServeiSchema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    getattr(ATDocument, 'schema', Schema(())).copy() + \
    schema.copy()
    
ServeiSchema['relatedItems'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}


class Servei(OrderedBaseFolder, ATFolder, ATDocument):
    """
    """
    security = ClassSecurityInfo()
    implements(IServei)

    meta_type = 'Servei'
    _at_rename_after_creation = True

    schema = ServeiSchema
    
    def listaServiciosfinal(self):
        """Return a list of metadata fields from portal_catalog.
        """    
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Servei',sort_on='Date',review_state='published')
        new_list=[]
        for f in mt:
            new_list.append(f.Title)
        return new_list

    def enlace(self):        
        obj=[]
        lista=[]
        lista = self.getListaservei1()
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Servei')       
        for i in lista:
            for j in mt:
                if i==j.Title:
                    obj.append(j)
        return obj

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
    def enlacefaq(self):
        var = self.getId()
        lista=[]
        obj=[] 
        portal_catalog = getToolByName(self, 'portal_catalog')          
        lista_faqs = portal_catalog.searchResults(portal_type = 'ServeiFaq',sort_order = 'Title',review_state='published')              
        for i in lista_faqs:
            lista = i.getListaservei2
            lista1 = self.arregloobj(lista)                     
            for ii in lista1:
                if ii.getId==var:
                    obj.append(i)
        return obj
    
    
    def enlacenot(self):
        var = self.getId()
        portal_catalog = getToolByName(self, 'portal_catalog')          
        lista_not = portal_catalog.searchResults(portal_type = 'Notificacions',sort_order = 'Title',review_state='published')       
        lista=[]
        obj=[]        
        for i in lista_not:
            lista = i.getListaservei3
            lista1 = self.arregloobj(lista)                    
            for ii in lista1:
                if ii.getId==var:
                    obj.append(i)
        return obj
    
registerType(Servei, PROJECTNAME)



