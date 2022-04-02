window.onscroll = function() {scroll()};
function scroll() {
    if ( document.documentElement.scrollTop > 480) {
        document.getElementById("navigation").style.cssText = "background:whitesmoke; opacity:0.7; "
    }
     else {
        document.getElementById("navigation").style.cssText =""
    }
};
function navbarOpen() {
    document.getElementById("navbarcont").style.left = "0vh"
};
function navbarClose() {
   document.getElementById("navbarcont").style.left = "100vh"
};

