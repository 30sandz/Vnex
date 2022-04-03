window.onscroll = function() {scroll()};
function scroll() {
    if ( document.documentElement.scrollTop > 480) {
        document.getElementById("navigation").style.cssText = "background:whitesmoke; opacity:0.7; "
        document.getElementById("content").style.cssText =""
    }
     else {
        document.getElementById("navigation").style.cssText =""
        document.getElementById("content").style.cssText = "position: relative;top: 11vh;left: -100vh; transition: 2s;"
    }
};
function navbarOpen() {
    document.getElementById("navbarcont").style.left = "0vh"
};
function navbarClose() {
   document.getElementById("navbarcont").style.left = "100vh"
};

