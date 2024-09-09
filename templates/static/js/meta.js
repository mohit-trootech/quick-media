$(document).ready(() => {
  /* Constants & Variables */
  const newPost = document.getElementById("newPost");
  const ajaxUrl = "/meta/ajax_update_instagram/";

  /* Toast Element */
  var myToastEl = document.getElementById("myToast");
  var myToast = new bootstrap.Toast(myToastEl, {
    animation: true,
    autohide: true,
    delay: 5000,
  });

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
        if (type != "PUT") {
          if (xhr.status == 200) {
            newPost.innerHTML = content + newPost.innerHTML;
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
        if (xhr.status == 205) {
          location.reload();
        }
        if (extraArguments) {
          btnDisableToggle(extraArguments);
          BtnActiveClassToggle(extraArguments);
        }
      },
      error: function (xhr, error, status) {
        if (extraArguments) {
          btnDisableToggle(extraArguments);
        }
        console.error(
          `An Error Occured with Status ${status} ${xhr.status}, ${xhr.responseText}`
        );
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

  /* Post Description Collapse Text Toggle */
  $(".feed-title-toggle").click((elem) => {
    elem.target.innerText == "Show Less"
      ? (elem.currentTarget.innerText = "Show More")
      : (elem.currentTarget.innerText = "Show Less");
  });
});
