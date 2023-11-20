from pickle import dump, load
from numpy import array
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidgetItem


def char_roman_to_number(char):
  match char:
    case "I": aux = 1
    case "V": aux = 5
    case "X": aux = 10
    case "L": aux = 50
    case "C": aux = 100
    case "D": aux = 500
    case "M": aux = 1000
  
  return aux

def roman_to_number(roman):
  decimal = 0
  l = len(roman) - 1
  for i in range(l):
    x = char_roman_to_number(roman[i])
    if char_roman_to_number(roman[i+1]) > x:
      decimal -= x
    else:
      decimal += x


  return decimal + char_roman_to_number(roman[l])

def Ajouter():
  roman = window.ro.text()
  number = window.no.text()
  if len(roman) != 1 or "IVXLCDM".find(roman) == -1:
    QMessageBox.critical(window, "Error", "Invalid roman number")
  elif not number.isdecimal():
    QMessageBox.critical(window, "Error", "Invalid decimal number")
  else:
    file = open("Files/Nombres.dat", mode="ab")
    e = dict()
    aux = char_roman_to_number(roman)
    if aux == int(number):
      e["rom"] = roman
      e["deci"] = int(number)
      dump(e, file)
      QMessageBox.information(window, "Success", "The roman number is added successfully!")
      window.ro.clear()
      window.no.clear()
    else:
      QMessageBox.critical(window, "Error", "The decimal number is not equal to the roman value")

    file.close()


def AfficherNbr():
  file = open("Files/Nombres.dat", mode="rb")
  eof = False
  window.TW.setRowCount(0)
  i = 0
  while not eof:
    try:
      e = load(file)
      window.TW.insertRow(i)
      window.TW.setItem(i, 0, QTableWidgetItem(e["rom"]))
      window.TW.setItem(i, 1, QTableWidgetItem(str(e["deci"])))
      i += 1
    except:
      eof = True
  file.close()


def valid(line):
  if "IVXLCDM".find(line[0]) == -1 or line[len(line)-1] != "?" or line.find("++") != -1 or line.find("--") != -1 or line.find("==") != -1:
    return False
  else:
    i = 0
    test = True
    while test and i < len(line):
      test = "IVXLCDM +-=?".find(line[i]) != -1
      i += 1
    return test


def insertion_sort(ar, n):
  for i in range(1, n):
    aux1 = ar[i]["sum"]
    aux2 = ar[i]["line"]
    j = i
    while j > 0 and aux1 > ar[j-1]["sum"]:
      ar[j]["sum"] = ar[j-1]["sum"]
      ar[j]["line"] = ar[j-1]["line"]
      j -= 1
    ar[j]["sum"] = aux1
    ar[j]["line"] = aux2


def display_text(file_path, mode):
  window.LW.clear()
  file = open(file_path, mode=mode)
  line = file.readline()
  while line != "\n":
    window.LW.addItem(line)
    line = file.readline()
  file.close()

def Afficher():
  op_radio = window.op.isChecked()
  res_radio = window.res.isChecked()
  if op_radio:
    display_text("Files/operations.txt", 'r')
  elif res_radio:
    text_file = open("Files/operations.txt", mode="r")
    res_file = open("Files/resultats.txt", mode="w")
    line = text_file.readline()
    while line != "\n":
      line = line[:len(line) - 1]
      if valid(line):
        line = line[:line.find("=")]
        s = 0
        res = ""
        sign = 1
        ok = len(line) > 0
        while ok:
          if line[0] == "-":
            sign = -1
            res += " - "
            line = line[2:]
          elif line[0] == "+":
            sign = 1
            line = line[2:]
            res += " + "
          else:
            pos_space = line.find(" ")
            roman = line[:pos_space]
            decimal = roman_to_number(roman)
            s += decimal * sign
            res += str(decimal)
            line = line[pos_space+1:]
          ok = len(line) > 0

        res += " = " + str(s) + "\n"
      else:
        res = "Operation Invalide\n"
      res_file.write(res)
      line = text_file.readline()
    res_file.write("\n")
    res_file.close()
    text_file.close()

    cb = window.CB.currentIndex()
    if cb == 0:
      QMessageBox.critical(window, "Error", "Choose whether to sort or not")
    
    elif cb == 1:
      display_text("Files/resultats.txt", 'r')
    else:
      text_file = open("Files/resultats.txt", mode="r")  
      ar = array([{}] * 100, dtype=dict)
      line = text_file.readline()
      n = 0
      while line != "\n":
        if line != "Operation Invalide\n":
          ar[n] = dict()
          ar[n]["sum"] = int(line[line.find("= ")+2:len(line)-1])
          ar[n]["line"] = line
          n += 1
        line = text_file.readline()
      text_file.close()
      window.LW.clear()
      insertion_sort(ar, n)
      for i in range(n):
        window.LW.addItem(ar[i]["line"])
    

app = QApplication([])
window = loadUi("Files/GUI/roman_no.ui")
window.show()
window.B1.clicked.connect(Ajouter)
window.B2.clicked.connect(AfficherNbr)
window.B3.clicked.connect(Afficher)
app.exec_()
