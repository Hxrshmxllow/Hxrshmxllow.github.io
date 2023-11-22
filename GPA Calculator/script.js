function validate(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    if(username=="admin" && password=="user"){
        window.close("index.html");
        window.open("page.html");
    }
    else{
        alert("Login Failed");
    }
}  

