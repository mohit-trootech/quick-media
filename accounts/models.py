from django.db.models import (
    CharField,
    IntegerField,
    ImageField,
    Model,
    ForeignKey,
    ManyToManyField,
    CASCADE,
)
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from accounts.utils.constants import ModelConstants, Choices
from youtube.models import Tag, Category


# Create your models here.
class User(AbstractUser):
    age = IntegerField(null=True, blank=True)
    address = CharField(max_length=1024, null=True, blank=True)
    phone = PhoneNumberField(region="IN", null=True, blank=True)  # type: ignore
    gender = CharField(choices=Choices.GENDER_CHOICE.value, blank=True, null=True)
    profile = ImageField(
        upload_to=ModelConstants.PROFILE_UPLOAD_TO.value, blank=True, null=True
    )
    following = ManyToManyField(
        "self", blank=True, related_name="followers", symmetrical=False
    )

    def get_interests(self):
        return self.interests

    def get_followers(self):
        return self.followers.all()

    def get_following(self):
        return self.following.all()

    def get_total_posts(self):
        return self.posts.all()

    def get_posts(self):
        return self.posts.all()

    def get_saved_posts(self):
        return self.saves.all()

    def __str__(self):
        return "{username}".format(username=self.username)


class Interest(Model):
    user = ForeignKey(
        User, on_delete=CASCADE, related_name=ModelConstants.INTEREST_FK.value
    )
    category = ManyToManyField(Category, related_name=ModelConstants.INTEREST_FK.value)
    tag = ManyToManyField(Tag, related_name=ModelConstants.INTEREST_FK.value)

    def __str__(self):
        return "{user} Interests".format(user=self.user)
