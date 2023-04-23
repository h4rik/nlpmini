function validateForm() {
  var firstname = document.getElementById("firstname").value;
  var lastname = document.getElementById("lastname").value;
  var username = document.getElementById("username").value;
  var email = document.getElementById("email").value;
  var mobile = document.getElementById("mobile").value;
 

  
  // Regex pattern for mobile number validation
  var mobilePattern = /^\d{10}$/;

  // Regex pattern for email validation
  var emailPattern = /^\S+@\S+\.\S+$/;

  var isValid = true;

  // Validate first name
  if (firstname.trim() === "") {
    document.getElementById("firstnameError").innerHTML = "Please enter your first name";
    isValid = false;
  } else {
    document.getElementById("firstnameError").innerHTML = "";
  }

  // Validate last name
  if (lastname.trim() === "") {
    document.getElementById("lastnameError").innerHTML = "Please enter your last name";
    isValid = false;
  } else {
    document.getElementById("lastnameError").innerHTML = "";
  }

  // Validate username
  if (username.trim() === "") {
    document.getElementById("usernameError").innerHTML = "Please enter a username";
    isValid = false;
  } else if (username.length < 6) {
    document.getElementById("usernameError").innerHTML = "Username must be at least 6 characters long";
    isValid = false;
  } else {
    document.getElementById("usernameError").innerHTML = "";
  }

  

  // Validate email
  if (email.trim() === "") {
    document.getElementById("emailError").innerHTML = "Please enter your email";
    isValid = false;
  } else if (!emailPattern.test(email)) {
    document.getElementById("emailError").innerHTML = "Invalid email address";
    isValid = false;
  } else {
    document.getElementById("emailError").innerHTML = "";
  }

  // Validate mobile number
  if (mobile.trim() === "") {
    document.getElementById("mobileError").innerHTML = "Please enter your mobile number";
    isValid = false;
  } else if (!mobilePattern.test(mobile)) {
    document.getElementById("mobileError").innerHTML = "Invalid mobile number";
    isValid = false;
  } else {
    document.getElementById("mobileError").innerHTML = "";
  }

  

  return isValid;
}

