document.getElementById("loginForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    // var forgetPw = document.getElementById("forgetPasswordLink").value;
    // var signUp = document.getElementById("signUpLink").value;

    if (username === "admin" && password === "123456") {
      document.getElementById("message").textContent = "Đăng nhập thành công!";
    } else {
      document.getElementById("message").textContent = "Tên đăng nhập hoặc mật khẩu không chính xác!";
    }
    
    var signUpLink = document.getElementById("signUpLink");
    signUpLink.click();
  });


// document.getElementById("forgetPasswordLink").addEventListener("click", function(event) {
//     event.preventDefault();
//     window.location.href = "forget_password.html"; // Đường dẫn tới trang Forget Password
//   });
  
