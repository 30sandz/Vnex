function navbarOpen() {
    document.getElementById("navbarcont").style.left = "0vh"
};
function navbarClose() {
   document.getElementById("navbarcont").style.left = "100vh"
};

function data() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var error = document.getElementById("error")

if (username == "sandeep" && password == "sandeep") {
    alert("done");
    location.href = '/admin'
} 
else if (username == "admin" && password == "san") {
    alert("done");
    location.href = '/admin'
} 
else {
    error.style.cssText = "opacity: 0.9;";
    alert("invalid username or password");
    location.reload();
    }
    return 0;
};