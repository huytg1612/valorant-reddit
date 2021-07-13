import graphene


class TopicCreateInput(graphene.InputObjectType):
    name = graphene.String()
    description = graphene.String()
    background_color_code = graphene.String(default_value="#007bff")
    font_color_code = graphene.String(default_value="#ffffff")