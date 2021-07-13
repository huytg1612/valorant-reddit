import graphene


class PostCreateInput(graphene.InputObjectType):
    title = graphene.String()
    body = graphene.String()
    topic_ids = graphene.List(of_type=graphene.Int)