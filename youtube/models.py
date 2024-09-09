from django.db.models import (
    CharField,
    TextField,
    BigIntegerField,
    ForeignKey,
    CASCADE,
    ManyToManyField,
    DateTimeField,
)
from django_extensions.db.models import TitleDescriptionModel, TimeStampedModel
from youtube.utils.constants import Constants


class Region(TitleDescriptionModel):

    def __str__(self):
        return self.title


class Tag(TitleDescriptionModel):

    def __str__(self):
        return self.title


class Channel(TitleDescriptionModel, TimeStampedModel):
    published = DateTimeField(null=True, blank=True)
    channel_id = CharField(max_length=64)
    thumbnail = TextField(null=True, blank=True)
    views = BigIntegerField(null=True, blank=True)
    subscribers = BigIntegerField(null=True, blank=True)
    video_count = BigIntegerField(null=True, blank=True)
    region = ForeignKey(
        Region, on_delete=CASCADE, related_name=Constants.CHANNEL_RELATED_NAME.value
    )

    def __str__(self):
        return self.title


class Category(TitleDescriptionModel):

    def __str__(self):
        return self.title


class Video(TitleDescriptionModel, TimeStampedModel):
    published = DateTimeField(null=True, blank=True)
    video_id = CharField(max_length=64)
    thumbnail = TextField(null=True, blank=True)
    channel = ForeignKey(
        Channel, on_delete=CASCADE, related_name=Constants.VIDEO_RELATED_NAME.value
    )
    category = ForeignKey(
        Category, on_delete=CASCADE, related_name=Constants.VIDEO_RELATED_NAME.value
    )
    tags = ManyToManyField(Tag, related_name=Constants.VIDEO_RELATED_NAME.value)
    views = BigIntegerField(null=True, blank=True)
    like = BigIntegerField(null=True, blank=True)

    def __str__(self):
        return "{title} {video_id}".format(title=self.title, video_id=self.video_id)
