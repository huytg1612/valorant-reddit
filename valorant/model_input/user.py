import graphene


class UserCreateInput(graphene.InputObjectType):
    id = graphene.ID()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    avatar = graphene.String()
    password = graphene.String()

class UserUpdateInput(graphene.InputObjectType):
    first_name = graphene.String()
    last_name = graphene.String()
    avatar = graphene.String()

class UserChangePasswordInput(graphene.InputObjectType):
    password = graphene.String()

class UserLoginInput(graphene.InputObjectType):
    email = graphene.String()
    password = graphene.String()