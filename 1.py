a=int(input("Введите целое число:"))
b=int(input("Введите целое число:"))
c=int(input("Введите целое число:"))
d=int(input("Введите целое число:"))
if a>0 and b>0 and c>0 and d>0:
 if c<d and a<b and a<c and b<d:
  print("Да!")
 else: 
  print("Нет!")
else:
 print("Ошибка!")
 