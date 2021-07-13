from graphene_django import DjangoObjectType

from valorant.models import Topic


class TopicType(DjangoObjectType):
    class Meta:
        model = Topic