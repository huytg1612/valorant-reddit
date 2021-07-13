import graphene
from graphql_jwt.decorators import login_required

from valorant.model_input.post import PostCreateInput
from valorant.model_type.post import PostType
from valorant.models import Topic, Post


class CreatePost(graphene.Mutation):
    class Arguments:
        input = PostCreateInput(required=True)

    status = graphene.Int()
    post = graphene.Field(PostType)

    @login_required
    def mutate(self, info, input=None):
        status = 400
        user = info.context.user
        topics = []
        for topicId in input.topic_ids:
            topics.insert(1, Topic.objects.get(pk=topicId))

        post = Post(title=input.title, body=input.body, author=user, rate=0)
        post.save()
        post.topic.set(topics)
        status = 200

        return CreatePost(status=status, post=post)
