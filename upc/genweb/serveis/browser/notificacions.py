from Acquisition import aq_inner
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.CMFCore.utils import getToolByName
from upc.genweb.serveis.interfaces import INotificacions

from plone.memoize.instance import memoize

class NotificacionsView(BrowserView):
    """Default view of a notificacions
    """

    # This template will be used to render the view. An implicit variable
    # 'view' will be available in this template, referring to an instance
    # of this class. The variable 'context' will refer to the cinema folder
    # being rendered.

    __call__ = ViewPageTemplateFile('notificacions.pt')
