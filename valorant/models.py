from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # Delete not use field
    username = None
    last_login = None
    is_staff = None
    is_superuser = None

    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    avatar = models.URLField(default="https://firebasestorage.googleapis.com/v0/b/valorantreddit-bc761.appspot.com/o/user_avatar%2Fdefault_avatar.png?alt=media&token=3796a9f0-32f7-48c0-b6d4-fb4e71455fd6")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class Topic(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    background_color_code = models.CharField(max_length=20, default="#007bff")
    font_color_code = models.CharField(max_length=20, default="#ffffff")

class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(range(0, 5))
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    topic = models.ManyToManyField(Topic)

class Viewer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    viewer = models.ForeignKey(Viewer, on_delete=models.CASCADE)
    reply_to = models.ForeignKey(Viewer, on_delete=models.CASCADE, null=True, related_name="reply_to")
    tag_to = models.ManyToManyField(User)
    # content = models.TextField()
    content = RichTextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(range(0, 5), default=0)
    reply_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)