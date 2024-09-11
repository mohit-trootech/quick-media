$(document).ready(() => {
  /* Constants & Variables */
  const newPost = document.getElementById("newPost");
  const ajaxUrl = "/meta/ajax_update/";
  const postModalBody = document.getElementById("postModalBody");
  const newPagePosts = document.getElementById("newPagePosts");

  /* Toast Element */
  const createModalDiv = document.getElementById("postCreate");
  const myModalElem = new bootstrap.Modal(createModalDiv);

  /* Get CSRF Token */
  function getCsrf() {
    return (csrf_token = $('input[name="csrfmiddlewaretoken"]').val().trim());
  }

  /* Update Url Path */
  function updateUrlPath(url) {
    window.history.pushState({}, null, url);
  }
  /* Page Scroll to Top */
  function scrollToTop() {
    window.scrollTo(0, 0);
  }
  /* Element Toggle Disabled */
  function btnDisableToggle(id) {
    $("#" + id).toggleClass("disabled");
  }
  /* postRequest Ajax */
  function postRequest(data, url, extraArguments) {
    ajaxCall("POST", data, url, getCsrf(), extraArguments);
  }

  function BtnActiveClassToggle(id) {
    $("#" + id).toggleClass("active");
  }

  /* getRequest Ajax */
  function putRequest(data, url, extraArguments) {
    ajaxCall("PUT", data, url, getCsrf(), extraArguments);
  }

  function deleteRequest(data, url) {
    ajaxCall("DELETE", data, url, getCsrf());
  }

  /* Ajax Call & Response Handling */
  function ajaxCall(type, data, url, csrfToken, extraArguments) {
    $.ajax({
      url: url,
      type: type,
      data: data,
      headers: {
        "X-CSRFToken": csrfToken,
      },
      processData: false,
      contentType: false,
      enctype: "multipart/form-data",
      success: function (content, status, xhr) {
        if (xhr.status != 204) {
          if (type != "PUT") {
            if (xhr.status == 200) {
              if (data.includes("page")) {
                newPagePosts.innerHTML += content;
              } else {
                newPost.innerHTML = content + newPost.innerHTML;
              }
            } else {
              let newComment = $("#newComment-" + data.get("id"))[0];
              let newCommentOffcanvas = $(
                "#newCommentOffcavas-" + data.get("id")[0]
              );
              newComment.innerHTML = content + newComment.innerHTML;
              newCommentOffcanvas.innerHTML =
                content + newCommentOffcanvas.innerHTML;
            }
          }
        } else {
          postId = JSON.parse(data).id;
          $(`#post_${postId}`).hide(1000);
        }
        if (xhr.status == 205) {
          location.reload();
        }
        if (extraArguments) {
          btnDisableToggle(extraArguments);
          BtnActiveClassToggle(extraArguments);
        }
        myModalElem.hide(1000);
      },
      error: function (xhr, error, status) {
        if (extraArguments) {
          btnDisableToggle(extraArguments);
        }
        console.error(`An Error Occured with Status ${status} ${xhr.status}`);
        if (xhr.status == 403) {
          toastBody.innerHTML = xhr.responseText;
          myToast.show();
        }
      },
    });
  }

  /* Feed Instagram Update */
  $("#feedInstagram").click((event) => {
    event.preventDefault();
    postRequest({ type: "feed" }, ajaxUrl);
  });

  /* Instagram Post Create */
  $("#createPostForm").submit((event) => {
    event.preventDefault();
    let form = $("#createPostForm")[0];
    var data = new FormData(form);
    data.append("type", "create");
    if (data.get("title")) {
      btnDisableToggle("postCreateBtn");
      postRequest(data, ajaxUrl, "postCreateBtn");
      form.reset();
    }
  });

  /* Post Like */
  $(".fa-heart").click((event) => {
    event.preventDefault();
    const elem_id = event.target.id;
    btnDisableToggle(elem_id);
    data = { id: elem_id.split("-")[1], type: "like" };
    putRequest(JSON.stringify(data), ajaxUrl, elem_id);
  });

  /* Post Saved */
  $(".fa-bookmark").click((event) => {
    event.preventDefault();
    const elem_id = event.target.id;
    btnDisableToggle(elem_id);
    data = { id: elem_id.split("-")[1], type: "saved" };
    putRequest(JSON.stringify(data), ajaxUrl, elem_id);
  });

  /* Post Description Collapse Text Toggle */
  $(".createPostComment").submit((event) => {
    event.preventDefault();
    let form = event.target;
    var data = new FormData(form);
    if (data.get("comment")) {
      data.append("type", "comment");
      postRequest(data, ajaxUrl);
      form.reset();
    }
  });

  /* User Following Ass */
  $(".followBtn").click((event) => {
    event.preventDefault();
    id = event.target.id;
    btnDisableToggle(id);
    data = { id: id, type: "following" };
    putRequest(JSON.stringify(data), ajaxUrl, id);
  });

  /* Profile Post Modal */
  function ajaxCallWithoutForm(type, data, url, csrfToken) {
    $.ajax({
      url: url,
      type: type,
      data: data,
      headers: {
        "X-CSRFToken": csrfToken,
      },
      success: function (content, status, xhr) {
        const postModal = document.getElementById("postModal");
        const postModalElem = new bootstrap.Modal(postModal);
        postModalBody.innerHTML = content;
        postModalElem.show();
      },
      error: function (xhr, error, status) {
        console.error(`An Error Occured with Status ${status} ${xhr.status}`);
      },
    });
  }
  $(".profile_posts").click((event) => {
    event.preventDefault();
    const id = event.target.closest("a").id;
    data = { id: id, type: "post_modal" };
    ajaxCallWithoutForm("POST", data, ajaxUrl, getCsrf());
  });

  /* Post Description Collapse Text Toggle */
  $(".feed-title-toggle").click((elem) => {
    elem.target.innerText == "Show Less"
      ? (elem.currentTarget.innerText = "Show More")
      : (elem.currentTarget.innerText = "Show Less");
  });

  /* Infinite Scrolling */
  window.addEventListener("scroll", () => {
    const scrollTop = window.scrollY || window.pageYOffset;
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;
    if (scrollTop + windowHeight + 1 >= documentHeight) {
      if ($(".infiniteScrollNotVisited").length == 1) {
        let search = $(".infiniteScrollNotVisited")[0].search.slice(1);
        ajaxCall("GET", search, ajaxUrl, getCsrf());
        updateTriggerClassCss();
      }
    }
  });
  function updateTriggerClassCss() {
    const scrollElem = $(".infiniteScrollNotVisited");
    scrollElem.removeClass("infiniteScrollNotVisited");
    scrollElem.addClass("infiniteScrollVisited");
  }
  /* Delete Post */
  $(".post-dropdown-item").click((event) => {
    event.preventDefault();
    postId = event.target.id;
    data = { id: postId, type: "delete" };
    deleteRequest(JSON.stringify(data), ajaxUrl);
  });
});
