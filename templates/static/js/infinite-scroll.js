$(document).ready(() => {
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
});
