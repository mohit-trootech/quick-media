from faker import Faker
from meta.models import Post, PostImage
from requests import get
from django.core.files.base import ContentFile
from accounts.models import User
from random import choice

fake = Faker()
users = User.objects.all()
data = []
data_img = []


def create(count):
    for i in range(count):

        def create_bulk_posts(count):
            for _ in range(count):
                title = fake.catch_phrase()
                post = Post(title=title, user=choice(users))
                data.append(post)

                for _ in range(1, 3):
                    response = get("https://picsum.photos/1024/1024")
                    image_content = response.content
                    image_name = f"image_{_}.jpg"

                    post_img = PostImage(post=post)
                    post_img.image.save(
                        image_name, ContentFile(image_content), save=False
                    )

                    data_img.append(post_img)
            return "Done"

        create_bulk_posts(20)
        Post.objects.bulk_create(data)
        PostImage.objects.bulk_create(data_img)
        data.clear()
        data_img.clear()


create(100)
