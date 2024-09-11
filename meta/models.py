from django.db.models import ForeignKey, CASCADE, ManyToManyField, ImageField, Model
from accounts.models import User
from django_extensions.db.models import (
    TitleDescriptionModel,
    ActivatorModel,
    TimeStampedModel
)
from meta.utils.constants import (
    MetaModelsConstants,
    THUMBNAIL_PREVIEW_TAG,
    THUMBNAIL_PREVIEW_HTML,
)
from django.utils.html import format_html


    
   
    

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

    @property
    def thumbnail_preview(self):
        if self.post.image:
            return format_html(THUMBNAIL_PREVIEW_TAG.format(img=self.post.image.url))
        return format_html(THUMBNAIL_PREVIEW_HTML)

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
