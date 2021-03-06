# -*- coding: utf-8 -*-

import json
from ...gedcomx import Gedcomx
from ..client import Rel
from .gedcomxapplicationstate import GedcomxApplicationState
from .personstate import PersonState


class CollectionsState(GedcomxApplicationState):

    def __init__(self, session, request, response, access_token, state_factory):
        super(CollectionsState, self).__init__(session, request, response, access_token, state_factory)

    def reconstruct(self, request, response):
        return CollectionsState(self.session, request, response, self.accessToken, self.stateFactory)

    def getMainDataElement(self):
        return self.entity

    def getCollections(self):
        if self.entity is not None:
            return self.entity.collections

    def getSourceDescriptions(self):
        if self.entity is not None:
            return self.entity.sourceDescriptions

    def readCollection(self):
        link = self.getLink(Rel.COLLECTION)

        if link is None or link.href == "":
            return None

        request = self.createAuthenticatedGedcomxRequest("GET", url=link.href)
        return self.stateFactory.buildCollectionState(self.session, request, self.invoke(request), self.accessToken)

    def addCollection(self, collection):
        link = self.getLink(Rel.SELF)

        if link is None or link.href == "":
            return None

        entity = Gedcomx()
        entity.collections.append(collection)
        request = self.createAuthenticatedGedcomxRequest("POST", url=link.href)
        request.data = json.dumps(entity.to_dict())
        return self.stateFactory.buildCollectionState(self.session, request, self.invoke(request), self.accessToken)

