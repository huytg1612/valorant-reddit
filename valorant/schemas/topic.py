import graphene
from graphql_jwt.decorators import login_required

from valorant.model_input.topic import TopicCreateInput
from valorant.model_type.topic import TopicType
from valorant.models import Topic


class CreateTopic(graphene.Mutation):
    class Arguments:
        input = TopicCreateInput()

    status = graphene.Int()
    topic = graphene.Field(TopicType)

    @login_required
    def mutate(self, info, input=None):
        status = 400
        topic = Topic(name=input.name, description=input.description, background_color_code=input.background_color_code, font_color_code=input.font_color_code)
        topic.save()
        status = 200
        return CreateTopic(status=status, topic=topic)
