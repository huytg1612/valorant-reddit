import graphene
from graphene_django import DjangoObjectType

from valorant.model_type.topic import TopicType
from valorant.models import Post


class PostType(DjangoObjectType):
    class Meta:
        model = Post

class PostViewType(graphene.ObjectType):
    id = graphene.ID()
    title = graphene.String()
    body = graphene.String()
    topics = graphene.List(TopicType)
    numOfComments = graphene.Int()
    numOfViews = graphene.Int()

