from zope import schema
from zope.interface import Interface

from zope.app.container.constraints import contains
from zope.app.container.constraints import containers

from upc.genweb.serveis import upcgenwebserveisMessageFactory as _

class IServei(Interface):
    """A Logos Container
    """