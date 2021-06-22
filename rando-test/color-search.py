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
     print(res.json())
     l = res.json()["colors"][0]["name"]
     print(l)
   else:
     print("That color was too much for us to handle.")