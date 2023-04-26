# Задача: пользователь вводит с клавиатуры число,
# программа выводит все простые числа не превышающие этого числа 

def is_prime_number(value):
	'''
	определяет, является ли переданное ей число простым
	возвращает True или False
	'''	
	
	# счетчик делителей value
	counter_divs = 0

	# index это число в диапозоне от 2 до value-1
	index = 2

	# вычисляем количество делителей value
	while (counter_divs == 0) and (index < value):
		# проверяем, является ли index делителем value
		if value % index == 0: 
			# если да, то увеличиваем счетчик делителей на 1
			counter_divs += 1
		# берем следующее число для проверки 
		index += 1

	# если количество делителей value равно 0, то число value простое
	if counter_divs == 0:
	    return True
	else:
		return False

num = int(input("введите число "))
# выводим на экран простые числа
for i in range(2, num):
	if is_prime_number(i):
		print(i)
