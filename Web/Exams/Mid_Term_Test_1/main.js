function randint(min, max) {
  return Math.trunc(min + (max - min + 1) * Math.random());
}

function randstring() {
  var s = "";
  for (i = 0; i <= 7; i++) {
    s += String(randint(0, 9))
  }
  return s
}

function sameNum(x, num) {
  if (x == num) {
    alert("the same")
    return ''
  } else {
    s = x;
    for (i = 0; i <= 7; i++) {
      if (num.charAt(i) != x.charAt(i)) {
        if (num.indexOf(x.charAt(i)) > -1) {
          s += " //" + x.charAt(i) + " in the position " + i + " is not in the right place"
        }
        s = s.substr(0, i) + "-" + s.substr(i+1, s.length - i - 1)
      }
    }
    return s
  }
}

function check(no) {
  full_name = document.getElementById("name").value;
  var MAX_ESS = 8;
  do {
    var x = prompt("Enter 8 digits, you have " + MAX_ESS + " tries left.")
    while (isNaN(x) || x.length != 8) {
      var x = prompt("Error, please enter 8 digits, you have " + MAX_ESS + " tries left.")
    }
    var res = sameNum(x, no);
    if (res.length > 0) {
      MAX_ESS -= 1;
      res = x + res.substr(8, res.length - 8) + "// You have " + MAX_ESS + " tries left."
      alert(res);
      var test = false;
    } else {
      alert("yes")
      test = true;
      document.getElementById("p1").innerHTML = "Congratulations " + full_name + " You guessed right. The number is " + no
    }
  } while(MAX_ESS > 0 && !test)
  if (MAX_ESS == 0 && !test) {
    document.getElementById("p1").innerHTML = "Oops! Sorry" + full_name + " you didn't guess the number. The right number is " + no
  }
}

function deriver() {
  alert("Hello")
  var no = randstring();
  alert(no)
  check(no);
}
