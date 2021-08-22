var toTopButton = document.querySelector("#scrolll");
toTopButton.style.display = "none";//by default should be hidden
document.querySelector('body').onscroll = function(){//whenever they scroll
  if (window.scrollY > 80)//if scroll is 150px from top
    toTopButton.style.display = "block";//if they scroll down, show
  else
    toTopButton.style.display = "none";//if they scroll up, hide
};
