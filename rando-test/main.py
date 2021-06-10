import requests
while True:
  c = "https://api.color.pizza/v1/"
  i = input("Enter hexadecimal value (enter exit to exit): ")
  try:
   i1 = int(i, 16) <= 16777215
  except:
   if i == "exit":
     break
   else:
     print("Color not found. Try again.")
  else:
   if i1:
     if len(i) < 6:
      while len(i) < 6:
        i = "0" + i
     res = requests.get(c + i)
     print(res.text)
     l = res.text[20:]
     l2 = l.find("\"")
     print(l[:l2])
   else:
     print("That color was too much for us to handle.")