# импортируем нужные библеотеки
import random

# устанавливаем начальные значения
MAX_EFFORTS = 3
effort = 1
we_won = False
left_border = 1
right_border = 10

# начинаем игру и получаем число
print("игра началаcь")
input('задумайте число от 1 до 10, когда будете готовы нажмите enter')

# перебираем попытки
while effort <= MAX_EFFORTS:
	# выбираем случайное число
	number = random.randint(left_border , right_border)
	print(number)
	plear = input('это число < > = ')
	# сужаем диапазон поиска
	
	if plear == "=":
	    we_won = True	
	    break
	elif plear == "<":
		right_border = number - 1	
	else:
		left_border = number + 1
	
	effort += 1

# выводим на экран результат
if we_won:
	print('ура, я победил!')
else:
	print("я проиграл")