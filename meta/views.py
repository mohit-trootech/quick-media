from django.http import (
    HttpResponse,
    HttpResponseForbidden,
    JsonResponse,
)
from django.views.generic import *
from meta.utils.constants import (
    IMAGES,
    TemplateNames,
    TemplateNames,
    ContextNames,
    Messages,
    Urls,
    Errors,
    TYPE,
    COMMENT,
    STATUS,
    CREATE,
    POST,
    LIKE,
    SAVED,
    ID,
    FOLLOWING,
    USER,
    POSTS,
    COMMENTS,
    FOLLOWERS,
)
from meta.models import Post
from accounts.models import User
from django.contrib.messages import info
from accounts.forms import ProfileUpdateForm
from django.shortcuts import render
from meta.utils.utils import (
    file_type_check_for_image,
    check_if_user_already_liked_post,
    check_if_user_saved_post,
    create_post_comment,
    get_create_form_data,
    post_object_create,
    create_post_images_object,
    update_following_list,
)
from typing import Any


class Instagram(TemplateView):
    template_name = TemplateNames.INSTAGRAM_HOME.value

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context[POSTS] = (
            Post.objects.select_related(USER)
            .prefetch_related(LIKE, SAVED, IMAGES, COMMENTS)
            .all()
            .distinct()
        )
        return context


class AjaxUpdateInstagram(View):

    def post(self, request):
        type = request.POST.get(TYPE)
        if type == CREATE:
            title, images = get_create_form_data(request)
            try:
                file_type_check_for_image(images=images)
                post = post_object_create(title=title, user=request.user)
                create_post_images_object(post=post, images=images)
                page = render(
                    request,
                    TemplateNames.HOME_PAGE_TEMPLATE.value,
                    {POST: post},
                )
                return HttpResponse(page.content, status=200)
            except AssertionError:
                return HttpResponseForbidden(Errors.ASSERTION_ERROR_MESSAGE.value)
        elif type == COMMENT:
            comment = create_post_comment(self, request.POST)
            page = render(
                request, TemplateNames.COMMENT_CARD_TEMPLATE.value, {COMMENT: comment}
            )
            return HttpResponse(page.content, status=201)
        return HttpResponse(status=200)

    def put(self, request):
        from json import loads

        data = loads(request.body)
        if data.get(TYPE) == LIKE:
            if check_if_user_already_liked_post(self, data.get(ID)):
                return JsonResponse({STATUS: 204})
        elif data.get(TYPE) == SAVED:
            if check_if_user_saved_post(self, data.get(ID)):
                return JsonResponse({STATUS: 204})
        elif data.get(TYPE) == FOLLOWING:
            update_following_list(request, data.get(ID))
            return HttpResponse(status=205)
        return JsonResponse({STATUS: 200})


class ProfileView(UpdateView):
    template_name = TemplateNames.PROFILE_TEMPLATE.value
    form_class = ProfileUpdateForm
    model = User

    def get_object(self):
        """
        return the request user in object always
        """
        return User.objects.get(id=self.request.user.pk)

    def get_success_url(self) -> str:
        """
        returns success url if form is valid
        """
        info(self.request, Messages.PROFILE_UPDATE_SUCCESS.value)
        return Urls.INSTAGRAM_PROFILE.value.format(id=self.request.user.pk)


class InstagramProfileView(TemplateView):
    template_name = TemplateNames.PROFILE_TEMPLATE.value

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context[USER] = User.objects.prefetch_related(FOLLOWERS, FOLLOWING).get(
            username=kwargs.get(USER)
        )
        return context
