from turtle import ondrag
from django.db.models import *
from accounts.models import User
from django_extensions.db.models import (
    TitleDescriptionModel,
    ActivatorModel,
    TimeStampedModel,
)
from meta.utils.constants import MetaModelsConstants


class Post(TitleDescriptionModel, ActivatorModel, TimeStampedModel):
    user = ForeignKey(
        User, on_delete=CASCADE, related_name=MetaModelsConstants.POSTS_FK.value
    )
    like = ManyToManyField(User, related_name=MetaModelsConstants.LIKES.value)
    saved = ManyToManyField(User, related_name=MetaModelsConstants.SAVES.value)

    def get_post_comments(self):
        return self.comment.all()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]


class PostImage(Model):
    post = ForeignKey(
        Post, on_delete=CASCADE, related_name=MetaModelsConstants.POST_IMAGES.value
    )
    image = ImageField(
        null=True, blank=True, upload_to=MetaModelsConstants.POST_IMAGE_UPLOAD_TO.value
    )

    def __str__(self):
        return "{post} image".format(post=self.post)


class Comment(TitleDescriptionModel, TimeStampedModel):
    user = ForeignKey(
        User, on_delete=CASCADE, related_name=MetaModelsConstants.COMMENTS_FK.value
    )
    post = ForeignKey(
        Post, on_delete=CASCADE, related_name=MetaModelsConstants.COMMENTS_FK.value
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created"]
