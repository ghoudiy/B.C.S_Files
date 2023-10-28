from pickle import load, dump

def check(string):
  ok = string == "STOP"
  p = string.find("*")
  if not ok and 2 <= p <= len(string) - 3:
    x = string[:p]
    y = string[p+1:len(string)]
    ok = x.isdigit() and int(x) >= 10 and y.isdigit() and int(y) >= 10
  return ok    

def fill(file_path):
  ft = open(file_path, mode='w')
  string = ''
  n = 0
  while string != "STOP":
    string = input("Enter the " + str(n+1) + " X*Y: ")
    while not check(string):
      string = input("Enter the " + str(n+1) + " X*Y: ")
    if string != "STOP":
      ft.write(string + "\n")
      n += 1
  ft.close()
  return n

def figure_numbers(a, b):
  x = str(a)
  y = str(b)
  i = 0
  test = True
  while test and i < len(x):
    test = y.find(x[i]) != -1
    i += 1
  return test

def type_xy(x, y):
  test1 = figure_numbers(x, y)
  test2 = figure_numbers(y, x)
  string = "Not brothers"
  if test1 and test2:
    string = "Brothers"
  elif test1:
    string = "stepbrother side x"
  elif test2:
    string = "stepbrother side y"
  return string

def generate(file2_path, file_path, n):
  ft = open(file_path, mode='r')
  f = open(file2_path, mode='wb')
  for i in range(n):
    string = ft.readline()
    p = string.find("*")
    e = dict()
    e["x"] = string[:p]
    e["y"] = string[p+1:len(string)-1]
    e["type"] = type_xy(e["x"], e["y"])
    dump(e, f)

  ft.close()
  f.close()

def display(file2_path):
  f = open(file2_path, mode="rb")
  eof = False
  while not eof:
    try:
      e = load(f)
      print("X =", e['x'])
      print("Y =", e['y'])
      print("Type =", e['type'])
    except:
      eof = True

n = fill("Files/numbers.txt")
generate("Files/brothers.dat", "Files/numbers.txt", n)
display("Files/brothers.dat")
