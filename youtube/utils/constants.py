from enum import Enum


class YoutubeTemplateConstants(Enum):
    YOUTUBE_HOME_TEMPLATE = "youtube/youtube-feed.html"
    YOUTUBE_STREAMING_TEMPLATE = "youtube/streaming-page.html"


class YoutubeUrlsReverse(Enum):
    YOUTUBE_HOME_REVERSE = "youtube-home"
    YOUTUBE_REQUEST_REVERSE = "request-page"
    YOUTUBE_STREAM_VIDEO_REVERSE = "youtube-stream"


class YoutubeApiUrls(Enum):
    YOUTUBE_API_VIDEOS_CHART_REGION_KEY = "https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults={items}&chart={chart}&regionCode=IN&type=video&key={key}"
    YOUTUBE_API_VIDEO_DATA = (
        "https://www.googleapis.com/youtube/v3/search?type=video&key={key}"
    )
    YOUTUBE_VIDEO_CATEGORIES = "https://www.googleapis.com/youtube/v3/videoCategories?key={key}regionCode={region}"
    YOUTUBE_VIDEO_WITH_ID = "https://www.googleapis.com/youtube/v3/videos?part=snippet,statistics&id={id}&key={key}"
    YOUTUBE_CHANNEL_WITH_ID = "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={id}&key={key}"
    YOUTUBE_VIDEO_SEARCH = "https://www.googleapis.com/youtube/v3/search?type=video&q={search}&maxResults=50&key={key}"


class YoutubeUrls(Enum):
    YOUTUBE_CHANNEL = "https://www.youtube.com/channel/{id}"
    YOUTUBE_VIDEO_WATCH = "https://www.youtube.com/watch?v={id}"


class YoutubeApiConstants(Enum):
    CHART_POPULAR = "mostPopular"
    SEARCH_VALUE = "searchValue"


class Constants(Enum):
    RANDOM_DATE = "?"
    VIDEO_ID_JSON = "videoId"
    CURRENT_VIDEO_CONTEXT_NAME = "current_video"
    RELATED_VIDEOS_CONTEXT_NAME = "videos"
    CHANNEL_RELATED_NAME = "channels"
    VIDEO_RELATED_NAME = "videos"
    YOUTUBE_CONTEXT_NAME = "videos"
    ENV = ".env"
    ID = "id"
    NOT_FOUND = "Try Again With Proper URL Content Not Available"
    YOUTUBE_HOME_URL = "/youtube/"
    STATUS = "status"


class YoutubeApiKeys(Enum):
    YOUTUBE_API_KEY = "YOUTUBE_API_KEY"
    # YOUTUBE_API_KEY = "YOUTUBE_API_KEY_EXTRA"


class YoutubeJsonResponseConstants(Enum):
    ITEMS = "items"
    SNIPPET = "snippet"
    STATISTICS = "statistics"
    HIGH = "high"
    URL = "url"
    PUBLISHED_AT = "publishedAt"
    THUMBNAILS = "thumbnails"
    SUBSCRIBERS_COUNT = "subscribersCount"
    VIDEO_COUNT = "videoCount"
    COUNTRY = "country"
    UNKNOWN = "unknown"
    CHANNEL_ID = "channelId"
    CATEGORY_ID = "categoryId"
    LIKE_COUNT = "likeCount"
    VIEW_COUNT = "viewCount"
    VIDEO_ID = "videoId"


class YoutubeModelFieldConstants(Enum):
    TITLE = "title"
    DESCRIPTION = "description"
    PUBLISHED = "published"
    CHANNEL_ID = "channel_id"
    THUMBNAIL = "thumbnail"
    VIEWS = "views"
    SUBSCRIBERS = "subscribers"
    REGION = "region"
    TAGS = "tags"
    VIDEO_ID = "video_id"
    VIDEO_COUNT = "video_count"
    CHANNEL = "channel"
    CATEGORY = "category"
    LIKE = "like"
    TAG = "tag"
