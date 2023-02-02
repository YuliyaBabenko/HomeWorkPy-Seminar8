import math
  
def cos(num):
    return math.cos(math.radians(num))
 
 
def sin(num):
    return math.sin(math.radians(num))
 
 
def tg(num):
    return math.tan(math.radians(num))
 
 
def ctg(num):
    return 1 / math.tan(math.radians(num))
 
 
def ln(num):
    return math.log(math.radians(num))
 
calc = input('Введите выражение для вычисления: ')
 
calc = calc.replace("^", "**")
 
print(f'Ваш результат: {eval(calc)}')
