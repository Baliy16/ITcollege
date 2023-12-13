kimbo = "Перший текст, \" використовую спецсимволи,\nа також розрив строки"
array = ['23'*23, {"here": "we go"}, (23, 43, 66)]

print(f"My string is {kimbo}, my array is {array}")

for i in range(len(array)):
    print(f"На позиції {i} знаходиться {array[i]}")

list = [1, 2, "1", [1, 2], "2", (1, 2)]
for i in list:
    if type(list[i]) == tuple:
        print("{i} -- кортедж") 
    elif type(list[i]) == array:
        print("{i} -- список")
    else: 
        print("{i} -- не кортедж і не список")

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))

print("Оригінальний список:", numbers)
print("Список з квадратами чисел:", squared_numbers)
