# -*- coding: utf-8 -*-

__author__ = 'Sandeep S <codereverser@gmail.com>'
__version__ = '0.1'
__date__ = '02-July-2014'

from .extensibledata import ExtensibleData
from .resourcereference import ResourceReference


class OnlineAccount(ExtensibleData):
    """An online account for a web application.

    :ivar str accountName: The name of the account.
    :ivar ResourceReference serviceHomePage: The homepage of the service that provides this account
    """

    def __init__(self, obj=None):
        self.accountName = ""
        self.serviceHomePage = ResourceReference()
        super(OnlineAccount, self).__init__(obj)

