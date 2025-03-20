listed_num = []

while True :
  number = input("Chose a number:")
  if number.lower() == "done":
      break
   else :
      num = int(number)
      listed_num.append(int(num))
     
if len(listed_num) > 0 :
   for i in listed_num :
      if i % 2 == 0:
       print("the first even number was", i)
       break
if listed_num:
  print("The numbers you entered are:", listed_num)

else:
  print("No numbers were entered by the user")
