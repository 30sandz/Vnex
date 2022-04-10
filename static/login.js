function daa() {
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    var error = document.getElementById("error")

    if (username == "sandeep" && password == "sandeep") {
    alert("done");
    location.href = 'login'
    } else if (username == "admin" && password == "san") {
    alert("done");
    window.location.href = 'admin'
    } else {
    error.style.cssText = "opacity: 0.9;";
    alert("invalid username or password");
    location.reload();
    }
};