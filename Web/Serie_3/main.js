function check_password(pass) {
  var i = 0;
  var test = true;
  pass = pass.toUpperCase()
  while (test && i < pass.length) {
    alert(pass.charAt(i))
    alert(i)
    var test = "A" <= pass.charAt(i) <= "Z" || "0" <= pass.charAt(i) <= "9";
    alert("appartient de a..z = " + String("A" <= pass.charAt(i) <= "Z"))
    alert("appartient de 0..9 = " + String("0" <= pass.charAt(i) <= "9"))
    alert("test = " + test)
    i++;
  }
  return test && pass.length == 8;
}


function check() {
  var password = document.getElementById("pass").value;
  var male = document.getElementById("male").checked;
  var female = document.getElementById("female").checked;
  var country = document.getElementById("country").selectedIndex;
  var html = document.getElementById("html5").checked;
  var css = document.getElementById("css3").checked;
  var js = document.getElementById("js").checked;

  if (! check_password(password)) {
    alert("The password is not valid")
    return false;
  
  } else if (male + female == 0) {
    alert("Please choose your gender")
    return false;
  
  } else if (country == 0) {
    alert("Please choose your country");
    return false;
  
  } else if (html + css + js == 0) {
    alert("Please choose at least one course")
    return false;
  }
}