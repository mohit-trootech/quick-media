from django.http import HttpResponse
from django.views.generic import *
from youtube.utils.constants import (
    YoutubeApiConstants,
    YoutubeTemplateConstants,
    YoutubeModelFieldConstants,
    Constants,
)
from typing import Any
from youtube.utils.utils import (
    create_user_interests,
    get_related_video_shuffled_data_based_on_user_interest,
    get_related_video_shuffled_data_based_on_current_video_category,
    get_related_video_shuffled_data_based_on_search_query,
    get_current_video_object,
    handle_api_response,
    get_user_interest,
    get_related_video_shuffled_data_complete,
    handle_api_response_for_video_searching,
)
from django.shortcuts import render
from threading import Thread
from django.core.paginator import Paginator


class YoutubeHomeView(TemplateView):
    template_name = YoutubeTemplateConstants.YOUTUBE_HOME_TEMPLATE.value
    select_related_channel = YoutubeModelFieldConstants.CHANNEL.value
    select_related_category = YoutubeModelFieldConstants.CATEGORY.value
    prefetch_related_tag = YoutubeModelFieldConstants.TAGS.value

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_value = (
            self.request.GET.get(YoutubeApiConstants.SEARCH_VALUE.value) or None
        )
        if search_value:
            videos_data = get_related_video_shuffled_data_based_on_search_query(
                search_value.lower()
            )
        else:
            interests = get_user_interest(self.request.user)
            if interests is not None:
                videos_data = get_related_video_shuffled_data_based_on_user_interest(
                    interests=interests
                )
            else:
                videos_data = get_related_video_shuffled_data_complete()
        paginator = Paginator(
            videos_data,
            18,
        )
        page_number = self.request.GET.get("page") or 1
        page_obj = paginator.get_page(page_number)
        context[Constants.RELATED_VIDEOS_CONTEXT_NAME.value] = page_obj
        task = Thread(target=handle_api_response)
        task.start()
        return context


class YoutubeRequestHandle(View):
    select_related_channel = YoutubeModelFieldConstants.CHANNEL.value
    select_related_category = YoutubeModelFieldConstants.CATEGORY.value
    prefetch_related_tag = YoutubeModelFieldConstants.TAGS.value

    def post(self, request):
        id = request.POST.get(Constants.ID.value)
        context = {}
        current_video_object = get_current_video_object(id)
        create_user_interests(
            self,
            tags=current_video_object.tags.all(),
            category_id=current_video_object.category.id,
        )
        context[Constants.CURRENT_VIDEO_CONTEXT_NAME.value] = current_video_object
        context[Constants.RELATED_VIDEOS_CONTEXT_NAME.value] = (
            get_related_video_shuffled_data_based_on_current_video_category(
                current_video_object.category
            )
        )
        page = render(
            request, YoutubeTemplateConstants.YOUTUBE_STREAMING_TEMPLATE.value, context
        )
        return HttpResponse(page.content, {Constants.STATUS.value: 200})

    def get(self, request):
        context = {}
        searchValue = (
            self.request.GET.get(YoutubeApiConstants.SEARCH_VALUE.value) or None
        )
        if self.request.GET.get("page"):
            if searchValue:
                videos_data = get_related_video_shuffled_data_based_on_search_query(
                    searchValue.lower()
                )
            else:
                interests = get_user_interest(self.request.user)
                if interests is not None:
                    videos_data = (
                        get_related_video_shuffled_data_based_on_user_interest(
                            interests=interests
                        )
                    )
                else:
                    videos_data = get_related_video_shuffled_data_complete()
            paginator = Paginator(
                videos_data,
                18,
            )
            page_number = self.request.GET.get("page") or 1
            page_obj = paginator.get_page(page_number)
            context[Constants.RELATED_VIDEOS_CONTEXT_NAME.value] = page_obj
            page = render(request, "youtube/videos.html", context)
            return HttpResponse(page.content, status=200)
        context[Constants.RELATED_VIDEOS_CONTEXT_NAME.value] = (
            get_related_video_shuffled_data_based_on_search_query(searchValue)
        )

        page = render(
            request, YoutubeTemplateConstants.YOUTUBE_HOME_TEMPLATE.value, context
        )
        task = Thread(
            target=handle_api_response_for_video_searching, args=(searchValue,)
        )
        task.start()
        return HttpResponse(page.content, {Constants.STATUS.value: 204})


class StreamVideo(TemplateView):
    template_name = YoutubeTemplateConstants.YOUTUBE_STREAMING_TEMPLATE.value
    select_related_channel = YoutubeModelFieldConstants.CHANNEL.value
    select_related_category = YoutubeModelFieldConstants.CATEGORY.value
    prefetch_related_tag = YoutubeModelFieldConstants.TAGS.value

    def get_context_data(self, *args, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        current_video_object = get_current_video_object(
            self.kwargs.get(YoutubeModelFieldConstants.VIDEO_ID.value)
        )
        context[Constants.CURRENT_VIDEO_CONTEXT_NAME.value] = current_video_object
        context[Constants.RELATED_VIDEOS_CONTEXT_NAME.value] = (
            get_related_video_shuffled_data_based_on_current_video_category(
                current_video_object.category
            )
        )
        return context
