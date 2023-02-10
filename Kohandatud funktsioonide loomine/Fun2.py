from math import *
def bank():




def season(month):
"""
функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), 
и возвращающую время года, которому этот месяц принадлежит (talv, kevad, suvi или sügis).
"""
if month in (1,2,12):
   print("Talv")
elif month in (3,4,5): 
	print("Sügis")
elif month in (6,7,8): 
	print("Suvi")
elif month in (9,10,11): 
	print("sügis")
else:
	print("Viga")
return month





def square(a:int)->str:
'''
функция square, принимающую 1 аргумент — сторону квадрата, 
и возвращающую 3 значения (с помощью кортежа): 
периметр квадрата, площадь квадрата и диагональ квадрата.
'''
p = 4*a
s = a*a
d = (a**2) / 2
d = d**0.5	
k = (p, s, d)	
return k




def is_year_leap(year)->str:
'''
Написать функцию is_year_leap, 
принимающую 1 аргумент — год, и возвращающую True, если год високосный,
 и False иначе.
'''

while True:
   if x%4 == 0:
		if x%400 == 0:
			print("True")
		elif x%100 != 0:
			print("True")
		else:
			print("False")
		else:
			print("False") 	
    return is_year_leap




def arithmetic(a:int,b:int,tehe:str):
"""функцию arithmetic, принимающую 3 аргумента:
 первые 2 - числа, третий - операция, которая должна быть произведена над ними.
 Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на второе).
 В остальных случаях вернуть строку "Неизвестная операция".
"""
   if ari == "+":
       v=(a+b)
   elif ari== "-":
       v=(a-b)
   elif ari== "*":
       v=(a*b)
   elif ari== "/":
       v=(a/b)
		
   else:
       print("Неизвестная операция")
   return v

