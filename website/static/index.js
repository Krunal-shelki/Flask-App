let active = window.location.href.split("/")[3];

document.querySelectorAll(".main-nav-link").forEach((link) => {
  if (active == "") {
    document.querySelector(".home").classList.add("active");
  }
  if (active == "progress") {
    document.querySelector(".progs").classList.add("active");
  }
  if (active == "profile") {
    document.querySelector(".user-dropdown").classList.add("active");
  } else if (link.classList.contains(active)) {
    link.classList.add("active");
  }
});
