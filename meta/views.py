from django.http import (
    HttpRequest,
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
    POST_MODAL,
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
    get_post_with_id,
)
from typing import Any
from django.db.models import Q
from django.core.paginator import Paginator


class Instagram(TemplateView):
    template_name = TemplateNames.INSTAGRAM_HOME.value

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        posts = (
            Post.objects.select_related(USER)
            .prefetch_related(IMAGES, COMMENTS, LIKE, SAVED)
            .all()
            .exclude(like=self.request.user)
            .exclude(saved=self.request.user)
            .distinct()
        )
        paginator = Paginator(
            posts,
            10,
        )
        page_number = self.request.GET.get("page") or 1
        page_obj = paginator.get_page(page_number)
        context[POSTS] = page_obj
        return context


class AjaxUpdate(View):

    def get(self, request):
        context = {}
        context["users"] = User.objects.all()
        posts = (
            Post.objects.select_related(USER)
            .prefetch_related(IMAGES, COMMENTS, LIKE, SAVED)
            .all()
            .exclude(like=self.request.user)
            .exclude(saved=self.request.user)
            .distinct()
        )
        paginator = Paginator(
            posts,
            10,
        )
        page_number = self.request.GET.get("page") or 1
        page_obj = paginator.get_page(page_number)
        context[POSTS] = page_obj
        page = render(request, "facebook/home.html", context)
        return HttpResponse(page.content, status=200)

    def post(self, request):
        post_type = request.POST.get(TYPE)
        if post_type == CREATE:
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
        elif post_type == COMMENT:
            comment = create_post_comment(self, request.POST)
            page = render(
                request, TemplateNames.COMMENT_CARD_TEMPLATE.value, {COMMENT: comment}
            )
            return HttpResponse(page.content, status=201)
        elif post_type == POST_MODAL:
            post = get_post_with_id(id=request.POST.get(ID))
            page = render(request, TemplateNames.POST_CARD_TEMPLATE.value, {POST: post})
            return HttpResponse(page.content, status=200)
        return HttpResponse(status=400)

    def put(self, request):
        from json import loads

        try:
            data = loads(request.body)
            action_type = data.get(TYPE)
            post_id = data.get(ID)
            if action_type == LIKE:
                if check_if_user_already_liked_post(self, post_id):
                    return JsonResponse({STATUS: 204})
            elif action_type == SAVED:
                if check_if_user_saved_post(self, data.get(ID)):
                    return JsonResponse({STATUS: 204})
            elif action_type == FOLLOWING:
                update_following_list(request, data.get(ID))
                return HttpResponse(status=205)
            else:
                return HttpResponse(status=400)
        except Exception as e:
            return HttpResponse(status=500)

    def delete(self, request):
        try:
            import json

            data = json.loads(request.body)
            post_id = data.get(ID)
            post = get_post_with_id(id=post_id)
            post.delete()
            return HttpResponse(status=204)
        except Exception:
            return HttpResponse(status=500)


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


def is_ajax(request):
    """
    This utility function is used, as `request.is_ajax()` is deprecated.

    This implements the previous functionality. Note that you need to
    attach this header manually if using fetch.
    """
    return request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest"


class Facebook(TemplateView):
    template_name = TemplateNames.FACEBOOK_HOME.value

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["users"] = User.objects.all()
        posts = (
            Post.objects.select_related(USER)
            .prefetch_related(IMAGES, COMMENTS, LIKE, SAVED)
            .all()
            .exclude(like=self.request.user)
            .exclude(saved=self.request.user)
            .distinct()
        )
        paginator = Paginator(
            posts,
            10,
        )
        page_number = self.request.GET.get("page") or 1
        page_obj = paginator.get_page(page_number)
        context[POSTS] = page_obj
        return context


class FacebookProfileView(TemplateView):
    template_name = TemplateNames.FACEBOOK_PROFILE_TEMPLATE.value

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context[USER] = User.objects.prefetch_related(FOLLOWERS, FOLLOWING).get(
            username=kwargs.get(USER)
        )
        context[POSTS] = (
            Post.objects.select_related(USER)
            .prefetch_related(IMAGES)
            .filter(user=context[USER])
        )
        context["saved_posts"] = (
            Post.objects.select_related(USER)
            .prefetch_related(IMAGES)
            .filter(Q(user=context[USER]) & Q(saved__in=[context[USER].id]))
            .distinct()
        )
        return context
