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
from upc.genweb.serveis.interfaces import IServeiFaq
from upc.genweb.serveis.config import PROJECTNAME

schema = Schema((                
         
         LinesField('listaservei2',
                    required=False,
                    vocabulary='listaServicios',
                    enforceVocabulary=True,
                    widget=InAndOutWidget(
                            label="Lista de Servicios",
                            label_msgid="label_custom_view_fields",
                            description="Select which fields to display when "
                            "'Display as Table' is checked.",
                            description_msgid="help_custom_view_fields",
                            i18n_domain = "plone"),
         ),
                                      
                                             

  ),
)  

faqSchema = getattr(ATDocument, 'schema', Schema(())).copy() + schema.copy()

faqSchema['description'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
faqSchema['relatedItems'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}

class ServeiFaq(ATDocument):
    """
    Documento para describir una Faq
    """

    security = ClassSecurityInfo()
    implements(IServeiFaq)

    meta_type = 'ServeiFaq'
    _at_rename_after_creation = True

    schema = faqSchema

    def listaServicios(self):
        """Return a list of metadata fields from portal_catalog.
        """    
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Servei',sort_on='Date',review_state='published')
        new_list=[]
        for f in mt:
            new_list.append(f.Title)
        new_list.sort()
        return new_list
        
    def enlace(self):
        obj=[]
        lista=[]
        lista = self.getListaservei2()
        portal_catalog = getToolByName(self, 'portal_catalog')
        mt = portal_catalog.searchResults(portal_type = 'Servei')
        
        for i in lista:
            for j in mt:
                if i==j.Title:
                    obj.append(j)
        return obj
    
registerType(ServeiFaq, PROJECTNAME)
