const url = `/youtube/request_page/`;
const mainDiv = document.getElementById("youtubeMain");
const newVideosDiv = document.getElementById("newVideos");
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
    success: function (content, status, xhr) {
      if (typeof data == "string") {
        newVideosDiv.innerHTML += content;
      } else {
        mainDiv.innerHTML = content;
        scrollToTop();
        updateUrlPath(
          data.id
            ? `/youtube/${data["id"]}/`
            : `/youtube/?searchValue=${data["searchValue"]}`
        );
      }
    },
    error: function (xhr, error, status) {
      console.error(`An Error Occured with Status ${status} ${xhr.status}`);
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
    elem.currentTarget.innerText == "Show More"
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
        ajaxCall("GET", search, url, getCsrf());
        updateTriggerClassCss();
      }
    }
  });
  function updateTriggerClassCss() {
    const scrollElem = $(".infiniteScrollNotVisited");
    scrollElem.removeClass("infiniteScrollNotVisited");
    scrollElem.addClass("infiniteScrollVisited");
  }
});
