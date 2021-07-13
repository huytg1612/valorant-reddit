import graphene
from graphene_django import DjangoObjectType

from valorant.model_type.user import UserType
from valorant.model_type.viewer import ViewerType
from valorant.models import Viewer, User, Comment

class CommentType(DjangoObjectType):
    class Meta:
        model = Comment

class CommentViewType(graphene.ObjectType):
    id = graphene.ID()
    viewer = graphene.String()
    reply_to = graphene.String()
    tag_to = graphene.List(of_type=graphene.String)
    content = graphene.String()
    comment_date = graphene.DateTime()
    rate = graphene.Int()
    reply_comment = graphene.Field(CommentType)