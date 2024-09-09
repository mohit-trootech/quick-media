const url = `/youtube/request_page/`;
const mainDiv = document.getElementById("youtubeMain");
function getCsrf() {
  return (csrf_token = $('input[name="csrfmiddlewaretoken"]').val().trim());
}

function updateUrlPath(url) {
  window.history.pushState({}, null, url);
}
function scrollToTop() {
  window.scrollTo(0, 0);
}
function playVideo(id) {
  event.preventDefault();
  postRequest({ id: id });
}

function ajaxCall(type, data, csrfToken) {
  $.ajax({
    url: url,
    type: type,
    data: data,
    headers: {
      "X-CSRFToken": csrfToken,
    },
    success: function (content, status) {
      mainDiv.innerHTML = content;
      scrollToTop();
      updateUrlPath(
        data.id
          ? `/youtube/${data["id"]}/`
          : `/youtube/?searchValue=${data["searchValue"]}`
      );
    },
    error: function (xhr, error, status) {
      console.error(
        `An Error Occured with Status ${xhr.status}, ${xhr.responseText}`
      );
    },
  });
}

function postRequest(data) {
  ajaxCall("POST", data, getCsrf());
}

function getRequest(data) {
  ajaxCall("GET", data, getCsrf());
}

$(document).ready(() => {
  $("#youtubeSearch").submit((event) => {
    event.preventDefault();
    const searchValue = document.getElementById("searchOnYoutube").value;
    getRequest({ searchValue: searchValue });
  });
  $("#videoDetailBtn").click((elem) => {
    elem.currentTarget.innerText == "Show Less"
      ? (elem.currentTarget.innerText = "Show More")
      : (elem.currentTarget.innerText = "Show Less");
  });
});
