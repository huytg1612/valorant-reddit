from graphene_django import DjangoObjectType

from valorant.models import User


class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude = ("password",)