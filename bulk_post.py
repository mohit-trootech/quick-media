from faker import Faker
from meta.models import Post, PostImage
from requests import get
from django.core.files.base import ContentFile
from accounts.models import User
from random import choice

fake = Faker()



def fake_user(count):
    data = {'username':[], 'objects':[]}
    for _ in range(count):
        first_name=fake.user_name()
        last_name=fake.last_name()
        username=first_name
        password = fake.password()
        email = fake.email()
        if username not in data['username']:
            data['username'].append(username)
            data['objects'].append(User(first_name=first_name, last_name=last_name, username=username, password=password, email=email))
    return data['objects']



def create(count):
    users = User.objects.all()
    data = []
    data_img = []
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

        create_bulk_posts(10)
        Post.objects.bulk_create(data)
        PostImage.objects.bulk_create(data_img)
        data.clear()
        data_img.clear()

# Generate i User Objects
User.objects.bulk_create(fake_user(100))
# Generate Multiple of 10 Posts i*10 Examples 100*10=1000
create(100)
