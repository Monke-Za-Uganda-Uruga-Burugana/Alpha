import requests
while True:
  c = "https://api.color.pizza/v1/"
  i = input("Enter hexadecimal value: ")
  try:
    i1 = int(i, 16) <= 16777215
  except:
    if i == "exit":
      break
    else:
      print("\033[92mColor not found. Try again.")
  else:
    if i1:
      if len(i) < 6:
        while len(i) < 6:
          i = "0" + i
      res = requests.get(c + i)
      l = str(str(res.content)[22:])
      l2 = l.find("\"")
      print("\033[92m"+l[:l2]+"\033[0m")
    else:
      print("That color was too much for us to handle.")