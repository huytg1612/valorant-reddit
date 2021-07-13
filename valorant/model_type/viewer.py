from graphene_django import DjangoObjectType

from valorant.models import Viewer


class ViewerType(DjangoObjectType):
    class Meta:
        model = Viewer