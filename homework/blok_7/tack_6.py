a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
summ = 0  # считаем ссумму кратных чисел
quantity = 0  #считаем количество кратных чисел
for number in range(a, b):
  if number % 3 == 0: # проверяем кратность 
    summ += number # суммируем все кратные числа
    quantity += 1 # считаем сколько раз прошла кратность
print('Среднее арифметическое всех чисел кратных 3 равна: ', summ / quantity)