import graphene
from graphql_jwt.decorators import login_required

from valorant.model_input.user import UserLoginInput, UserUpdateInput, UserChangePasswordInput, UserCreateInput
from valorant.model_type.user import UserType
from valorant.models import User, Topic, Viewer, Post, Comment

class Register(graphene.Mutation):
    class Arguments:
        input = UserCreateInput(required=True)

    status = graphene.Int()
    user = graphene.Field(UserType)

    def mutate(root, info, input=None):
        status = 200
        user_instance = User(first_name=input.first_name, last_name=input.last_name, email=input.email,
                             password=input.password)
        user_instance.set_password(input.password)
        user_instance.save()
        return Register(status=status, user=user_instance)


class UpdateUser(graphene.Mutation):
    class Arguments:
        input = UserUpdateInput(required=True)

    status = graphene.Int()
    user = graphene.Field(UserType)

    @login_required
    def mutate(root, info, input=None):
        status = 400
        user = info.context.user

        if user.is_authenticated:
            status = 200
            if input.first_name:
                user.first_name = input.first_name
            if input.last_name:
                user.last_name = input.last_name
            if input.avatar:
                user.avatar = input.avatar
            user.save()
            return UpdateUser(status=status, user=user)

        status = 403
        return UpdateUser(status=status, user=None)


class ChangeUserPassword(graphene.Mutation):
    class Arguments:
        input = UserChangePasswordInput(required=True)

    status = graphene.Int()
    user = graphene.Field(UserType)

    @login_required
    def mutate(root, info, input=None):
        status = 400
        user = info.context.user
        if user:
            status = 200
            user.set_password(input.password)
            user.save()
            return ChangeUserPassword(status=status, user=user)

        status = 404
        return ChangeUserPassword(status=status, user=None)