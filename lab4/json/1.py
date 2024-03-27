import re

txt = open ("berr.txt", "r")


x = re.search("[A-Z]", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
  