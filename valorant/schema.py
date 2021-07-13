import graphene
import graphql_jwt
from graphene import ObjectType
from graphql_jwt.decorators import login_required

from valorant.model_type.comment import CommentViewType
from valorant.model_type.post import PostType, PostViewType
from valorant.model_type.topic import TopicType
from valorant.model_type.user import UserType
from valorant.models import Topic, Post, Viewer, Comment
from valorant.schemas.post import CreatePost
from valorant.schemas.topic import CreateTopic
from valorant.schemas.user import Register, UpdateUser, ChangeUserPassword

class Query(ObjectType):
    user = graphene.Field(UserType)
    topic = graphene.List(TopicType, name=graphene.String(default_value=""))
    post = graphene.List(PostViewType, title=graphene.String(default_value=""), id=graphene.ID(default_value=None))
    comment = graphene.List(CommentViewType, post_id=graphene.Int(required=True))

    @login_required
    def resolve_user(self, info, **kwargs):
        if info.context.user.is_authenticated:
            return info.context.user

        return None

    def resolve_topic(self, info, name, **kwargs):
        return Topic.objects.filter(name__icontains=name)

    def resolve_post(self, info, title, id, **kwargs):
        post = []
        if id:
            posts = Post.objects.filter(pk=id)
        else:
            posts = Post.objects.filter(title__icontains=title)

        results = []
        for post in posts:
            viewers = Viewer.objects.filter(post=post)
            numOfViews = len(viewers)
            numOfComments = 0
            for viewer in viewers:
                comments = Comment.objects.filter(viewer=viewer)
                numOfComments += len(comments)

            model = PostViewType(id=post.id, title=post.title, body=post.body, topics=post.topic.all(), numOfViews=numOfViews, numOfComments=numOfComments)
            results.insert(1, model)

        return results

    def resolve_comment(self, info, post_id, **kwargs):
        if post_id:
            result = []
            post = Post.objects.get(pk=post_id)
            viewers = Viewer.objects.filter(post=post)
            for viewer in viewers:
                comments = Comment.objects.filter(viewer=viewer)
                for comment in comments:
                    model = CommentViewType(id=comment.id, rate=comment.rate, content=comment.content, reply_to=comment.viewer.user.email, viewer=comment.viewer,
                                            comment_date=comment.comment_date, tag_to=comment.tag_to, reply_comment=comment.reply_comment)
                    result.insert(1, model)

            return result
        return None
class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    delete_token_cookie = graphql_jwt.DeleteJSONWebTokenCookie.Field()

    register = Register.Field()
    update_user = UpdateUser.Field()
    change_user_password = ChangeUserPassword.Field()

    create_topic = CreateTopic.Field()

    create_post = CreatePost.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
