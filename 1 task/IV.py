array = ['23'*23, {"here": "we go"}, (23, 43, 66)]
for i in list:
    if type(list[i]) == tuple:
        print("{i} -- кортедж") 
    elif type(list[i]) == array:
        print("{i} -- список")
    else: 
        print("{i} -- не кортедж і не список")