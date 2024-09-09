from multiprocessing import Process
from accounts.models import Interest
from youtube.models import Region, Channel, Category, Video, Tag
from youtube.utils.constants import (
    YoutubeApiUrls,
    YoutubeApiKeys,
    YoutubeJsonResponseConstants,
    YoutubeModelFieldConstants,
    Constants,
)
from requests import get
from dotenv import dotenv_values
from django.db.models import Q

config = dotenv_values(Constants.ENV.value)
api_key = config.get(YoutubeApiKeys.YOUTUBE_API_KEY.value)


def get_category_data(id: int):
    """
    get category data with id

    :param id: int
    """
    return Category.objects.get(id=id)


def get_list_or_create_tag_data(tags: list):
    """
    get tags objects list & if not exist create one and return the queryset of objects

    :param tags: list
    """
    tags_list = []
    for tag in tags:
        tags_list.append(Tag.objects.get_or_create(title=tag)[0])
    return tags_list


def get_or_create_region_data(title: str):
    """
    get region if not exist create one and return region object

    :param title: str
    """
    return Region.objects.get_or_create(title=title)[0]


def serialize_channel_data(data_json: dict, index: int) -> dict:
    """
    serialize channel data in required format

    :param data_json: dict
    :param index: int
    :return: dict
    """
    data = data_json.get(YoutubeJsonResponseConstants.ITEMS.value)[index]
    title = data.get(YoutubeJsonResponseConstants.SNIPPET.value).get(
        YoutubeModelFieldConstants.TITLE.value
    )
    description = data.get(YoutubeJsonResponseConstants.SNIPPET.value).get(
        YoutubeModelFieldConstants.DESCRIPTION.value
    )
    published = data.get(YoutubeJsonResponseConstants.SNIPPET.value).get(
        YoutubeJsonResponseConstants.PUBLISHED_AT.value
    )
    channel_id = data.get(Constants.ID.value)
    thumbnail = (
        data.get(YoutubeJsonResponseConstants.SNIPPET.value)
        .get(YoutubeJsonResponseConstants.THUMBNAILS.value)
        .get(YoutubeJsonResponseConstants.HIGH.value)
        .get(YoutubeJsonResponseConstants.URL.value)
    )
    views = data.get(YoutubeJsonResponseConstants.STATISTICS.value).get(
        YoutubeJsonResponseConstants.VIEW_COUNT.value
    )
    subscribers = data.get(YoutubeJsonResponseConstants.STATISTICS.value).get(
        YoutubeJsonResponseConstants.SUBSCRIBERS_COUNT.value
    )
    video_count = data.get(YoutubeJsonResponseConstants.STATISTICS.value).get(
        YoutubeJsonResponseConstants.VIDEO_COUNT.value
    )
    region = get_or_create_region_data(
        data.get(YoutubeJsonResponseConstants.SNIPPET.value).get(
            YoutubeJsonResponseConstants.COUNTRY.value,
            YoutubeJsonResponseConstants.UNKNOWN.value,
        )
    )
    return {
        YoutubeModelFieldConstants.TITLE.value: title,
        YoutubeModelFieldConstants.DESCRIPTION.value: description,
        YoutubeModelFieldConstants.PUBLISHED.value: published,
        YoutubeModelFieldConstants.CHANNEL_ID.value: channel_id,
        YoutubeModelFieldConstants.THUMBNAIL.value: thumbnail,
        YoutubeModelFieldConstants.VIEWS.value: views,
        YoutubeModelFieldConstants.SUBSCRIBERS.value: subscribers,
        YoutubeModelFieldConstants.VIDEO_COUNT.value: video_count,
        YoutubeModelFieldConstants.REGION.value: region,
    }


def fetch_create_and_get_channel_data(id: str):
    """
    fetch channel data in json format and update the model for respective channel object

    :param id: str
    """
    data = get(
        YoutubeApiUrls.YOUTUBE_CHANNEL_WITH_ID.value.format(id=id, key=api_key)
    ).json()
    serialized_data = serialize_channel_data(data, 0)
    channel = Channel.objects.create(
        title=serialized_data.get(YoutubeModelFieldConstants.TITLE.value),
        description=serialized_data.get(YoutubeModelFieldConstants.DESCRIPTION.value),
        published=serialized_data.get(YoutubeModelFieldConstants.PUBLISHED.value),
        channel_id=serialized_data.get(YoutubeModelFieldConstants.CHANNEL_ID.value),
        thumbnail=serialized_data.get(YoutubeModelFieldConstants.THUMBNAIL.value),
        views=serialized_data.get(YoutubeModelFieldConstants.VIEWS.value),
        subscribers=serialized_data.get(YoutubeModelFieldConstants.SUBSCRIBERS.value),
        video_count=serialized_data.get(YoutubeModelFieldConstants.VIDEO_COUNT.value),
        region=serialized_data.get(YoutubeModelFieldConstants.REGION.value),
    )
    return channel


def get_channel_data(channel_id: str):
    """
    get channel data, if not exist create one and return

    :param channel_id: _description_
    """
    try:
        channel = Channel.objects.get(channel_id=channel_id)
    except Channel.DoesNotExist:
        channel = fetch_create_and_get_channel_data(id=channel_id)
    return channel


def serialize_video_data(data_json: dict, index: int) -> dict:
    """
    serialize video data in required format

    :param data_json: dict
    :param index: int
    :return: dict
    """
    data = data_json.get(YoutubeJsonResponseConstants.ITEMS.value)[index]
    title = data.get(YoutubeJsonResponseConstants.SNIPPET.value).get(
        YoutubeModelFieldConstants.TITLE.value
    )
    description = data.get(YoutubeJsonResponseConstants.SNIPPET.value).get(
        YoutubeModelFieldConstants.DESCRIPTION.value
    )
    published = data.get(YoutubeJsonResponseConstants.SNIPPET.value).get(
        YoutubeJsonResponseConstants.PUBLISHED_AT.value
    )
    video_id = data.get("id")
    thumbnail = (
        data.get(YoutubeJsonResponseConstants.SNIPPET.value)
        .get(YoutubeJsonResponseConstants.THUMBNAILS.value)
        .get(YoutubeJsonResponseConstants.HIGH.value)
        .get(YoutubeJsonResponseConstants.URL.value)
    )
    channel = get_channel_data(
        data.get(YoutubeJsonResponseConstants.SNIPPET.value).get(
            YoutubeJsonResponseConstants.CHANNEL_ID.value
        )
    )
    category = get_category_data(
        id=int(
            data.get(YoutubeJsonResponseConstants.SNIPPET.value).get(
                YoutubeJsonResponseConstants.CATEGORY_ID.value
            )
        )
    )
    like = data.get(YoutubeJsonResponseConstants.STATISTICS.value).get(
        YoutubeJsonResponseConstants.LIKE_COUNT.value
    )
    views = data.get(YoutubeJsonResponseConstants.STATISTICS.value).get(
        YoutubeJsonResponseConstants.VIEW_COUNT.value
    )
    tags = get_list_or_create_tag_data(
        data.get(YoutubeJsonResponseConstants.SNIPPET.value).get(
            YoutubeModelFieldConstants.TAGS.value,
            [YoutubeJsonResponseConstants.UNKNOWN.value],
        )
    )
    return {
        YoutubeModelFieldConstants.TITLE.value: title,
        YoutubeModelFieldConstants.DESCRIPTION.value: description,
        YoutubeModelFieldConstants.PUBLISHED.value: published,
        YoutubeModelFieldConstants.VIDEO_ID.value: video_id,
        YoutubeModelFieldConstants.THUMBNAIL.value: thumbnail,
        YoutubeModelFieldConstants.CHANNEL.value: channel,
        YoutubeModelFieldConstants.CATEGORY.value: category,
        YoutubeModelFieldConstants.LIKE.value: like,
        YoutubeModelFieldConstants.VIEWS.value: views,
        YoutubeModelFieldConstants.TAGS.value: tags,
    }


def create_video_data_with_id_if_not_exist(id: int):
    """
    create video data if not exist in database

    :param id: int
    """
    if not Video.objects.filter(video_id=id).exists():
        data = get(
            YoutubeApiUrls.YOUTUBE_VIDEO_WITH_ID.value.format(id=id, key=api_key)
        ).json()
        serialized_data = serialize_video_data(data, 0)
        video = Video.objects.create(
            title=serialized_data.get(YoutubeModelFieldConstants.TITLE.value),
            description=serialized_data.get(
                YoutubeModelFieldConstants.DESCRIPTION.value
            ),
            published=serialized_data.get(YoutubeModelFieldConstants.PUBLISHED.value),
            video_id=serialized_data.get(YoutubeModelFieldConstants.VIDEO_ID.value),
            thumbnail=serialized_data.get(YoutubeModelFieldConstants.THUMBNAIL.value),
            channel=serialized_data.get(YoutubeModelFieldConstants.CHANNEL.value),
            category=serialized_data.get(YoutubeModelFieldConstants.CATEGORY.value),
            like=serialized_data.get(YoutubeModelFieldConstants.LIKE.value),
            views=serialized_data.get(YoutubeModelFieldConstants.VIEWS.value),
        )
        video.tags.add(
            *serialized_data.get(
                YoutubeModelFieldConstants.TAGS.value,
            )
        )
        return video


def create_user_interests(self, tags: list, category_id: int) -> None:
    """
    create user interest based on videos category_id & tags

    :param tags: list
    :param category_id: int
    """
    interest = Interest.objects.get_or_create(user=self.request.user)[0]
    interest.tag.add(*tags)
    interest.category.add(category_id)
    interest.save()


def get_related_video_shuffled_data_based_on_user_interest(interests):
    """
    get related video shuffle data based on user interests

    :param interests:
    """
    from random import shuffle

    select_related_channel = YoutubeModelFieldConstants.CHANNEL.value
    select_related_category = YoutubeModelFieldConstants.CATEGORY.value
    prefetch_related_tag = YoutubeModelFieldConstants.TAGS.value
    result = list(
        Video.objects.select_related(
            select_related_channel,
            select_related_category,
        )
        .prefetch_related(prefetch_related_tag)
        .filter(
            Q(tags__in=interests.tag.all()) & Q(category__in=interests.category.all())
        )
        .distinct()
    )
    shuffle(result)
    return result


def get_related_video_shuffled_data_based_on_current_video_category(category):
    """
    get related video shuffle data based on video category

    :param category:
    """
    from random import shuffle

    select_related_channel = YoutubeModelFieldConstants.CHANNEL.value
    select_related_category = YoutubeModelFieldConstants.CATEGORY.value
    prefetch_related_tag = YoutubeModelFieldConstants.TAGS.value
    result = list(
        (
            Video.objects.select_related(
                select_related_channel,
                select_related_category,
            )
            .prefetch_related(prefetch_related_tag)
            .filter(Q(category=category))
            .distinct()
        )
    )
    shuffle(result)
    return result


def get_related_video_shuffled_data_based_on_search_query(search):
    """
    get related video shuffle data based on user search

    :param search:
    """
    from random import shuffle

    select_related_channel = YoutubeModelFieldConstants.CHANNEL.value
    select_related_category = YoutubeModelFieldConstants.CATEGORY.value
    prefetch_related_tag = YoutubeModelFieldConstants.TAGS.value
    result = list(
        (
            Video.objects.select_related(
                select_related_channel,
                select_related_category,
            )
            .prefetch_related(prefetch_related_tag)
            .filter(Q(title__icontains=search))
            .distinct()
        )
    )
    shuffle(result)
    return result


def get_related_video_shuffled_data_complete():
    """
    get related video shuffle data complete

    :param search:
    """
    from random import shuffle

    select_related_channel = YoutubeModelFieldConstants.CHANNEL.value
    select_related_category = YoutubeModelFieldConstants.CATEGORY.value
    prefetch_related_tag = YoutubeModelFieldConstants.TAGS.value
    result = list(
        (
            Video.objects.select_related(
                select_related_channel,
                select_related_category,
            )
            .prefetch_related(prefetch_related_tag)
            .all()
            .distinct()
        )
    )
    shuffle(result)
    return result


def get_current_video_object(video_id: str):
    """
    get current video object based on video id

    :param video_id: str
    """
    select_related_channel = YoutubeModelFieldConstants.CHANNEL.value
    select_related_category = YoutubeModelFieldConstants.CATEGORY.value
    prefetch_related_tag = YoutubeModelFieldConstants.TAGS.value
    return (
        Video.objects.select_related(
            select_related_channel,
            select_related_category,
        )
        .prefetch_related(
            prefetch_related_tag,
        )
        .get(video_id=video_id)
    )


def handle_api_response():
    """
    handle api response
    """
    from django.db import connections
    from multiprocessing import Process

    response = (
        get(YoutubeApiUrls.YOUTUBE_API_VIDEO_DATA.value.format(key=api_key))
        .json()
        .get(YoutubeJsonResponseConstants.ITEMS.value)
    )
    connections.close_all()
    for video in response:
        p = Process(
            target=create_video_data_with_id_if_not_exist,
            args=(
                video.get(Constants.ID.value).get(
                    YoutubeJsonResponseConstants.VIDEO_ID.value
                ),
            ),
        )
        p.start()


def handle_api_response_for_video_searching(searchValue):
    """
    handle api response
    """
    from django.db import connections
    from multiprocessing import Process

    response = (
        get(
            YoutubeApiUrls.YOUTUBE_VIDEO_SEARCH.value.format(
                search=searchValue, key=api_key
            )
        )
        .json()
        .get(YoutubeJsonResponseConstants.ITEMS.value)
    )
    connections.close_all()
    for video in response:
        p = Process(
            target=create_video_data_with_id_if_not_exist,
            args=(
                video.get(Constants.ID.value).get(
                    YoutubeJsonResponseConstants.VIDEO_ID.value
                ),
            ),
        )
        p.start()


def get_user_interest(user):
    """
    get logged in user interest

    :param user:
    """
    try:
        interests = user.get_interests().get()
        return interests
    except Interest.DoesNotExist:
        return None
